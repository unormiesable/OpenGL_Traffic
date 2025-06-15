from pygame import mixer

class Audio:
    def __init__(self, app):
        self.app = app
        mixer.init()
        mixer.music.load("audios/example.mp3")
        mixer.music.play(-1)
    
    def destroy(self):
        mixer.music.stop()