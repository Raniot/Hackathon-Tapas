from AudioPlayer import AudioPlayer
import time

def main():
    audio = AudioPlayer()
    audio.Play('FirstCheckpointReached.mp3')
    audio.Play('FirstCheckpointReached.mp3')
    time.sleep(2.3)
    audio.KillOtherSounds()
    # audio.PlayBlocking("SecondCheckpointReached.mp3")
    

if __name__ == "__main__":
    main()