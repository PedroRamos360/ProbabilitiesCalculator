import kivy
from kivy.uix.label import Label

kivy.require("1.9.1")


class CustomLabel(Label):
	def __init__(self, **kwargs):
		super(CustomLabel, self).__init__(**kwargs)
		self.font_name = "RobotoMono-Regular"
		self.font_size = 30
		self.width = 100
		self.height = 50
