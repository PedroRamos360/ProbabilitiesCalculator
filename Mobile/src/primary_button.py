import kivy
from kivy.uix.button import Button

kivy.require("1.9.1")


class PrimaryButton(Button):
	def __init__(self, **kwargs):
		super(PrimaryButton, self).__init__(**kwargs)
		self.font_name = "RobotoMono-Regular"
		self.size_hint = None, None
		self.width = 450
		self.height = 100
		self.center_x = 400
		self.font_size = 30
		self.color = 55.0/255, 57.0/255, 58.0/255, 1
		self.background_normal = ''
		self.background_color = (119.0/255, 182.0/255, 234.0/255, 1)
