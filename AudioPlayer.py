from playsound import playsound
from multiprocessing import Process
import time

class AudioPlayer:
    def __init__(self):
        self.SoundBasePath = "./Sounds/"
        self.FirstCheckpointReached = Process(target=self._play, args=(self.SoundBasePath + 'FirstCheckpointReached.mp3', ))
        self.SecondCheckpointReached = Process(target=self._play, args=(self.SoundBasePath + 'SecondCheckpointReached.mp3', ))
        self.FinalCheckpointReached = Process(target=self._play, args=(self.SoundBasePath + 'FinalCheckpointReached.mp3', ))
        self.CollissionWarning = Process(target=self._play, args=(self.SoundBasePath + 'CollisionWarning.mp3', ))
        self.RouteDeviation = Process(target=self._play, args=(self.SoundBasePath + 'RouteDeviation.mp3', ))
        self.SafeCross = Process(target=self._play, args=(self.SoundBasePath + 'SafeCross.mp3', ))
        self.UnsafeCross = Process(target=self._play, args=(self.SoundBasePath + 'UnsafeCross.mp3', ))
        self.IsPlaying = False

    def PlayBlocking(self, sound: str) -> None:
        self.KillOtherSounds()
        self._play(self.SoundBasePath + sound)

    def Play(self, sound: str) -> None:
        if sound == 'FirstCheckpointReached.mp3' and not self.FirstCheckpointReached.is_alive():
            self.FirstCheckpointReached = Process(target=self._play, args=(self.SoundBasePath + 'FirstCheckpointReached.mp3', ))
            self.KillOtherSounds()
            self.FirstCheckpointReached.start()
        elif sound == 'SecondCheckpointReached.mp3' and not self.SecondCheckpointReached.is_alive():
            self.SecondCheckpointReached = Process(target=self._play, args=(self.SoundBasePath + 'SecondCheckpointReached.mp3', ))
            self.KillOtherSounds()
            self.SecondCheckpointReached.start()
        elif sound == 'FinalCheckpointReached.mp3' and not self.FinalCheckpointReached.is_alive():
            self.FinalCheckpointReached = Process(target=self._play, args=(self.SoundBasePath + 'FinalCheckpointReached.mp3', ))
            self.KillOtherSounds()
            self.FinalCheckpointReached.start()
        elif sound == 'CollisionWarning.mp3' and not self.CollissionWarning.is_alive() and self.IsPlaying == False:
            self.CollissionWarning = Process(target=self._play, args=(self.SoundBasePath + 'CollisionWarning.mp3', ))
            self.CollissionWarning.start()
        elif sound == 'RouteDeviation.mp3' and not self.RouteDeviation.is_alive() and self.IsPlaying == False:
            self.RouteDeviation = Process(target=self._play, args=(self.SoundBasePath + 'RouteDeviation.mp3', ))
            self.RouteDeviation.start()
        elif sound == 'SafeCross.mp3' and not self.SafeCross.is_alive():
            self.SafeCross = Process(target=self._play, args=(self.SoundBasePath + 'SafeCross.mp3', ))
            self.KillOtherSounds()
            self.SafeCross.start()
        elif sound == 'UnsafeCross.mp3' and not self.UnsafeCross.is_alive():
            self.UnsafeCross = Process(target=self._play, args=(self.SoundBasePath + 'UnsafeCross.mp3', ))
            self.KillOtherSounds()
            self.UnsafeCross.start()
        else:
            return

    def _play(self, sound):
        try:
            self.IsPlaying = True
            playsound(sound, block=True)
            self.IsPlaying = False
        except:
            pass

    def KillOtherSounds(self):
        try:
            if self.FirstCheckpointReached.is_alive():
                self.FirstCheckpointReached.terminate()
            if self.SecondCheckpointReached.is_alive():
                self.SecondCheckpointReached.terminate()
            if self.FinalCheckpointReached.is_alive():
                self.FinalCheckpointReached.terminate()
            if self.CollissionWarning.is_alive():
                self.CollissionWarning.terminate()
            if self.RouteDeviation.is_alive():
                self.RouteDeviation.terminate()
            if self.SafeCross.is_alive():
                self.SafeCross.terminate()
            if self.UnsafeCross.is_alive():
                self.UnsafeCross.terminate()
            time.sleep(0.2)
        except:
            pass