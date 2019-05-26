import re
from os.path import dirname, join

from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
from mycroft.util import play_wav, play_mp3

# TODO - Localization

class AnnounceSkill(MycroftSkill):
    @intent_handler(IntentBuilder("").require("Announce").require("Words"))
    def do_announce(self, message):
        # Remove everything up to the speak keyword and repeat that
        utterance = message.data.get('utterance')
        repeat = re.sub('^.*?' + message.data['Announce'], '', utterance)

        announce_chime = join(abspath(dirname(__file__)),
                              "sounds/chime.mp3")
        play_mp3(announce_chime)

        self.speak(repeat.strip())

    def stop(self):
        pass


def create_skill():
    return AnnounceSkill()
