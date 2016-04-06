from Config import Config
import pyttsx


class Voice(Config):

    def __init__(self, rate=120):
        self.engine = pyttsx.init()
        self.rate = rate
        self.engine.setProperty('rate', self.rate)
        self.msg = ""

    def set_rate(self):
        lp = self.load_pickle()
        self.engine.setProperty('rate', lp["RATE"])

    def set_vol(self):
        lp = self.load_pickle()
        self.engine.setProperty('volume', lp["VOL"])

    def set_lang(self):
        lp = self.load_pickle()
        self.engine.setProperty('voice', lp["LANG"])

    def speak(self, msg):
        lp = self.load_pickle()
        self.engine.say(lp["MSG"] + msg)
        self.engine.runAndWait()

    def one_thing(self):
        self.set_lang()
        self.set_vol()
        self.set_rate()
