from AudioPlayer import AudioPlayer
import time

def main():
    audio = AudioPlayer()
    audio.Play('RouteDeviation.mp3')
    audio.Play('RouteDeviation.mp3')
    time.sleep(2)
    audio.KillOtherSounds()
    # audio.PlayBlocking("SecondCheckpointReached.mp3")
    

if __name__ == "__main__":
    main()