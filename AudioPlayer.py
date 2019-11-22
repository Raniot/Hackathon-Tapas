from playsound import playsound

class AudioPlayer:
    def __init__(self):
        pass

    def play(self, filePath: str) -> None:
        playsound(filePath)