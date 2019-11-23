from Webcam import UsbWebcam
from AudioPlayer import AudioPlayer
from Yolo import Yolo
from cv2 import cv2
from Coordinate import Coordinate
from geopy.distance import geodesic
from threading import Thread
import time


def main():
    cam = UsbWebcam()
    ml = Yolo()
    coord = Coordinate()
    audio = AudioPlayer()

    navigation = Thread(target=CoordinateNavigation, args=(coord, audio))
    navigation.start()

    camera = Thread(target=CameraNavigation, args=(cam, ml, audio))
    camera.start()


def CoordinateNavigation(coord, audio):
    #                 Start,                   First,                 Second,                    Final
    checkpoints = [(56.171977, 10.187193), (56.171944,10.187414), (56.171927, 10.187406), (56.171837, 10.187364)]
    checkpointReached = 1
    file = open('data4.ubx', 'r')

    while True:
        try:
            line = file.readline()
            if not line:
                time.sleep(0.1)
            elif line.find('$GNGLL') >= 0 and len(line) == 51:
                # print(line)
                latitude = float(line[7:9]) + float(line[9:17])/60
                longitude = float(line[20:23]) + float(line[23:31])/60
                pos = (latitude, longitude)
                distToCheckpoint = geodesic(
                    pos, checkpoints[checkpointReached]).meters*100
                print(f"Distance to destination in cm: {distToCheckpoint}")

                if distToCheckpoint <= 50:
                    if(checkpointReached == len(checkpoints) - 1):
                        audio.Play("FinalCheckpointReached.mp3")
                        break
                    if(checkpointReached == len(checkpoints) - 2):
                        audio.Play("SecondCheckpointReached.mp3")
                        #Handle roadcrossing
                        break
                    else:
                        checkpointReached += 1
                        audio.Play("FirstCheckpointReached.mp3")

                distToLine = coord.minDistanceBetweenLineAndPoint(checkpoints[checkpointReached - 1][0], checkpoints[checkpointReached - 1][1], checkpoints[checkpointReached][0],
                                checkpoints[checkpointReached][1], latitude, longitude)

                if distToLine >= 50:
                    audio.Play("RouteDeviation.mp3")

        except:
            print(f"Failed to read line probably because of random char")


def CameraNavigation(cam, ml, audio):
    while True:
        frame = cam.GetFrame()
        image, objectClose = ml.ProcessImage(frame)
        if(objectClose):
            audio.Play("CollisionWarning.mp3")
            print('Object is close')
        cv2.imshow("Image", image)

        key = cv2.waitKey(20)
        if key == 27:  # exit on ESC
            break

    cam.CloseCamera()


if __name__ == "__main__":
    main()
