from Webcam import UsbWebcam
from AudioPlayer import AudioPlayer
from Yolo import Yolo
from cv2 import cv2 

def main():
    cam = UsbWebcam()
    ml = Yolo()

    #cam.GetFeed() #close by press on ESC
    
    # audio = AudioPlayer()
    # audio.play(r'D:\OneDrive\Computer Teknologi\TAPAS Hackathon\wickedsick.mp3')

    
    while True:
        frame = cam.GetFrame()
        image = ml.ProcessImage(frame)
        cv2.imshow("Image", image)
        
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break


    cam.CloseCamera()



if __name__ == "__main__":
    main()