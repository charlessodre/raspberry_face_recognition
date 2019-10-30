from gtts import gTTS
import os


class SpeakText(object):

    def __init__(self, audio_file='speak_text_file.mp3', audio_prog='mpg123'):
        self.file = audio_file
        self.audio_prog = audio_prog

    def speak(self, text, lang='pt-br'):
        tts = gTTS(text=text, lang=lang)
        tts.save(self.file)
        os.system(self.audio_prog + " " + self.file)
        os.remove(self.file)
