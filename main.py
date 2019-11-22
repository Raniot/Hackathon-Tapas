from MyWebcam import UsbWebcam
from AudioPlayer import AudioPlayer

def main():
    cam = UsbWebcam()
    
    #cam.GetFeed() #close by press on ESC
    
    frame = cam.GetFrame()
    cam.CloseCamera()

    audio = AudioPlayer()
    audio.play(r'D:\OneDrive\Computer Teknologi\TAPAS Hackathon\wickedsick.mp3')


if __name__ == "__main__":
    main()