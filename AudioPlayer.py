from playsound import playsound
from threading import Thread

class AudioPlayer:
    def __init__(self):
        self.FirstCheckpointReached = Thread()
        self.SecondCheckpointReached = Thread()
        self.FinalCheckpointReached = Thread()
        self.CollissionWarning = Thread()
        self.RouteDeviation = Thread()
        self.SafeCross = Thread()
        self.UnsafeCross = Thread()
        self.SoundBasePath = "./Sounds/"

    def Play(self, sound: str) -> None:
        if sound == 'FirstCheckpointReached.mp3' and not self.FirstCheckpointReached.is_alive():
            self.FirstCheckpointReached = Thread(target=playsound, args=(self.SoundBasePath + sound, ))
            self.FirstCheckpointReached.start()
        elif sound == 'SecondCheckpointReached.mp3' and not self.SecondCheckpointReached.is_alive():
            self.SecondCheckpointReached = Thread(target=playsound, args=(self.SoundBasePath + sound, ))
            self.SecondCheckpointReached.start()
        elif sound == 'FinalCheckpointReached.mp3' and not self.FinalCheckpointReached.is_alive():
            self.FinalCheckpointReached = Thread(target=playsound, args=(self.SoundBasePath + sound, ))
            self.FinalCheckpointReached.start()
        elif sound == 'CollisionWarning.mp3' and not self.CollissionWarning.is_alive():
            self.CollissionWarning = Thread(target=playsound, args=(self.SoundBasePath + sound, ))
            self.CollissionWarning.start()
        elif sound == 'RouteDeviation.mp3' and not self.RouteDeviation.is_alive():
            self.RouteDeviation = Thread(target=playsound, args=(self.SoundBasePath + sound, ))
            self.RouteDeviation.start()
        elif sound == 'SafeCross.mp3' and not self.SafeCross.is_alive():
            self.SafeCross = Thread(target=playsound, args=(self.SoundBasePath + sound, ))
            self.SafeCross.start()
        elif sound == 'UnsafeCross.mp3' and not self.UnsafeCross.is_alive():
            self.UnsafeCross = Thread(target=playsound, args=(self.SoundBasePath + sound, ))
            self.UnsafeCross.start()
        else:
            return
        