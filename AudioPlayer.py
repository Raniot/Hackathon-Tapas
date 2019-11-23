from playsound import playsound
import time

class AudioPlayer:
    def __init__(self):
        self.Timer = time.time()

    def Play(self, filePath: str) -> None:
        playsound(filePath, block=False)