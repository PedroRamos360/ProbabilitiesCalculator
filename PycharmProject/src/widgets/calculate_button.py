import kivy
from kivy.uix.button import Button

kivy.require("1.9.1")


class CalculateButton(Button):
	def __init__(self, **kwargs):
		super(CalculateButton, self).__init__(**kwargs)
		self.size_hint = None, None
		self.font_size = 20
		self.width = 250
		self.height = 50
		self.center_y = 250
		self.center_x = 220
		self.text = "Calculate"
