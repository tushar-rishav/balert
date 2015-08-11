import pyttsx


class voice:
	
	def __init__ (self, _ = 120):
		self.engine = pyttsx.init()
		self.rate = _
		self.engine.setProperty('rate', self.rate)
		self.msg = "Low Battery!"
	
	def set_rate(self,rate):
		self.engine.setProperty('rate', rate)

	def set_vol(self, volume):
		self.engine.setProperty('volume', volume)

	def set_lang(self, lang):
		self.engine.setProperty('voice', lang)
	
	def speak(self):
		self.engine.say(self.msg)
		self.engine.runAndWait()