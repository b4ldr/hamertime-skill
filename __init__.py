from pygame import mixer
from mycroft import MycroftSkill, intent_file_handler


class Hamertime(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        mixer.init()

    def initialize(self):
        self.mp3 = self.settings.get('mp3')
        mixer.music.load(self.mp3)

    @intent_file_handler('hamertime.intent')
    def handle_hamertime(self, message):
        mixer.music.play()

    def stop(self):
        mixer.music.stop()


def create_skill():
    return Hamertime()
