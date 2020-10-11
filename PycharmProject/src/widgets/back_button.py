import kivy
from kivy.uix.button import Button

kivy.require("1.9.1")


class BackButton(Button):
	def __init__(self, **kwargs):
		super(BackButton, self).__init__(**kwargs)
		self.size_hint = None, None
		self.font_size = 20
		self.width = 150
		self.height = 50
		self.center_y = 500
		self.x = 0
		self.text = "Back"
