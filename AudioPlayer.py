from playsound import playsound
from threading import Thread

class AudioPlayer:
    def __init__(self):
        self.thread = Thread()

    def Play(self, filePath: str) -> None:
        if not self.thread.is_alive():
            self.thread = Thread(target=playsound, args=(filePath, ))
            self.thread.start()
        