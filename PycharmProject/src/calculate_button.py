import kivy
from kivy.uix.button import Button

kivy.require("1.9.1")


class CalculateButton(Button):
	def __init__(self, **kwargs):
		super(CalculateButton, self).__init__(**kwargs)
		self.font_name = "RobotoMono-Regular"
		self.size_hint = 0.6, 0.12
		self.color = 0, 0, 0, 1
		self.pos_hint = {'center_x': 0.5, 'center_y': 0.3}
		self.background_normal = ''
		self.background_color = (128/255, 255/255, 125/255, 1)
		self.font_size = 30
		self.width = 450
		self.height = 70
		self.text = "Calculate"
