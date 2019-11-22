from cv2 import cv2

class UsbWebcam:
    def __init__(self):
        self.vc = cv2.VideoCapture(0)
        print('Initing Webcam')

    def CloseCamera(self):
        self.vc.release()

    def GetFrame(self):
        if self.vc.isOpened(): # try to get the first frame
            _, frame = self.vc.read()
            return frame

    def GetFeed(self):
        cv2.namedWindow("preview")

        if self.vc.isOpened(): # try to get the first frame
            rval, frame = self.vc.read()
        else:
            rval = False

        while rval:
            cv2.imshow("preview", frame)
            rval, frame = self.vc.read()
            key = cv2.waitKey(20)
            if key == 27: # exit on ESC
                break
        
        self.CloseCamera()
        cv2.destroyWindow("preview")
