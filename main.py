from MyWebcam import UsbWebcam

def main():
    cam = UsbWebcam()
    
    #cam.GetFeed() #close by press on ESC
    
    frame = cam.GetFrame()
    cam.CloseCamera()


if __name__ == "__main__":
    main()