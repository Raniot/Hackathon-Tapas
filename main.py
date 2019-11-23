from Webcam import UsbWebcam
from AudioPlayer import AudioPlayer
from Yolo import Yolo
from cv2 import cv2
from Coordinate import Coordinate
from geopy.distance import geodesic
from threading import Thread
import time

SAFE_PASSING = True

def main():
    cam = UsbWebcam()
    ml = Yolo()
    coord = Coordinate()
    audio = AudioPlayer()

    navigation = Thread(target=CoordinateNavigation, args=(coord, audio, cam, ml))
    navigation.start()

    camera = Thread(target=CameraNavigation, args=(cam, ml, audio))
    camera.start()


def CoordinateNavigation(coord, audio, cam, ml):
    #                 Start,                   First,                 Second,                    Final
    checkpoints = [(56.171977, 10.187193), (56.171938, 10.187448), (56.171915, 10.187440), (56.171832, 10.187397)]
    checkpointReached = 1
    file = open('data6.ubx', 'r')

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

                if distToCheckpoint <= 100:
                    if(checkpointReached == len(checkpoints) - 1):
                        audio.Play("FinalCheckpointReached.mp3")
                        print('Final Checkpoint reached')
                        break
                    if(checkpointReached == len(checkpoints) - 2):
                        print('Second Checkpoint reached')
                        audio.Play("SecondCheckpointReached.mp3")
                        global SAFE_PASSING
                        if(SAFE_PASSING == True):
                            print('Safe to cross')
                            audio.Play("SafeCross.mp3")
                            checkpointReached += 1
                        else:
                            print('Unsafe to cross')
                            audio.Play("UnsafeCross.mp3")
                    else:
                        checkpointReached += 1
                        print('First Checkpoint reached')
                        audio.Play("FirstCheckpointReached.mp3")

                distToLine = coord.minDistanceBetweenLineAndPoint(checkpoints[checkpointReached - 1][0], checkpoints[checkpointReached - 1][1], checkpoints[checkpointReached][0],
                                checkpoints[checkpointReached][1], latitude, longitude)

                if distToLine >= 70:
                    audio.Play("RouteDeviation.mp3")

        except:
            print(f"Failed to read line probably because of random char")


def CameraNavigation(cam, ml, audio):
    global SAFE_PASSING

    while True:
        frame = cam.GetFrame()
        image, objectClose, SAFE_PASSING = ml.ProcessImage(frame)
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
