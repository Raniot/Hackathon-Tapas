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
        self.IsPlaying = False

    def PlayBlocking(self, sound: str) -> None:
        playsound(self.SoundBasePath + sound, block=True)

    def Play(self, sound: str) -> None:
        if sound == 'FirstCheckpointReached.mp3' and not self.FirstCheckpointReached.is_alive():
            self.FirstCheckpointReached = Thread(target=self._play, args=(self.SoundBasePath + sound, ))
            self.KillOtherSounds()
            self.FirstCheckpointReached.start()
        elif sound == 'SecondCheckpointReached.mp3' and not self.SecondCheckpointReached.is_alive():
            self.SecondCheckpointReached = Thread(target=self._play, args=(self.SoundBasePath + sound, ))
            self.KillOtherSounds()
            self.SecondCheckpointReached.start()
        elif sound == 'FinalCheckpointReached.mp3' and not self.FinalCheckpointReached.is_alive():
            self.FinalCheckpointReached = Thread(target=self._play, args=(self.SoundBasePath + sound, ))
            self.KillOtherSounds()
            self.FinalCheckpointReached.start()
        elif sound == 'CollisionWarning.mp3' and not self.CollissionWarning.is_alive() and self.IsPlaying == False:
            self.CollissionWarning = Thread(target=self._play, args=(self.SoundBasePath + sound, ))
            self.CollissionWarning.start()
        elif sound == 'RouteDeviation.mp3' and not self.RouteDeviation.is_alive() and self.IsPlaying == False:
            self.RouteDeviation = Thread(target=self._play, args=(self.SoundBasePath + sound, ))
            self.RouteDeviation.start()
        elif sound == 'SafeCross.mp3' and not self.SafeCross.is_alive():
            self.SafeCross = Thread(target=self._play, args=(self.SoundBasePath + sound, ))
            self.KillOtherSounds()
            self.SafeCross.start()
        elif sound == 'UnsafeCross.mp3' and not self.UnsafeCross.is_alive():
            self.UnsafeCross = Thread(target=self._play, args=(self.SoundBasePath + sound, ))
            self.KillOtherSounds()
            self.UnsafeCross.start()
        else:
            return

    def _play(self, sound):
        self.IsPlaying = True
        playsound(sound, block=True)
        self.IsPlaying = False

    def KillOtherSounds(self):
        self.FirstCheckpointReached._stop()
        self.SecondCheckpointReached._stop()
        self.FinalCheckpointReached._stop()
        self.CollissionWarning._stop()
        self.RouteDeviation._stop()
        self.SafeCross._stop()
        self.UnsafeCross._stop()