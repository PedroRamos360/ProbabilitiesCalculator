import kivy
from kivy.uix.label import Label

kivy.require("1.9.1")


class CustomLabel(Label):
	def __init__(self, **kwargs):
		super(CustomLabel, self).__init__(**kwargs)
		self.size_hint = None, None
		self.font_size = 20
		self.width = 50
		self.height = 50
		self.center_y = 300
