from cv2 import cv2

class UsbWebcam:
    def __init__(self):
        print('Initiating Webcam...')
        self.vc = cv2.VideoCapture(0)
        print('Webcam initiated')
        

    def CloseCamera(self) -> None:
        self.vc.release()

    def GetFrame(self):
        _, image = self.vc.read()
        return image
            
            

    def GetFeed(self) -> None:
        try:
            cv2.namedWindow("preview")

            if self.vc.isOpened():
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

        finally:
            self.CloseCamera()
