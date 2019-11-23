from AudioPlayer import AudioPlayer
import time

def main():
    audio = AudioPlayer()
    audio.Play('CollisionWarning.mp3')
    audio.Play('CollisionWarning.mp3')
    time.sleep(2.3)
    audio.Play('CollisionWarning.mp3')
    audio.Play('CollisionWarning.mp3')
    time.sleep(5)
    # audio.KillOtherSounds()
    audio.Play('CollisionWarning.mp3')
    audio.Play('CollisionWarning.mp3')
    time.sleep(5)
    # audio.KillOtherSounds()
    audio.Play('CollisionWarning.mp3')
    audio.Play('CollisionWarning.mp3')
    time.sleep(5)
    # audio.PlayBlocking("SecondCheckpointReached.mp3")
    

if __name__ == "__main__":
    main()