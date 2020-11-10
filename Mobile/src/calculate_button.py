import kivy
from kivy.uix.button import Button

kivy.require("1.9.1")


class CalculateButton(Button):
	def __init__(self, **kwargs):
		super(CalculateButton, self).__init__(**kwargs)
		self.font_name = "RobotoMono-Regular"
		self.size_hint = None, None
		self.color = 55.0/255, 57.0/255, 58.0/255, 1
		self.pos_hint = {'center_x': 0.5, 'center_y': 0.3}
		self.background_normal = ''
		self.background_color = (119.0/255, 182.0/255, 234.0/255, 1)
		self.font_size = 40
		self.width = 550
		self.height = 150
		self.text = "Calculate"
