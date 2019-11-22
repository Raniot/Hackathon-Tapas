from MyWebcam import UsbWebcam

def main():
    cam = UsbWebcam()
    
    cam.GetFeed()


if __name__ == "__main__":
    main()