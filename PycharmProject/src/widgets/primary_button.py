import kivy
from kivy.uix.button import Button

kivy.require("1.9.1")


class PrimaryButton(Button):
	def __init__(self, **kwargs):
		super(PrimaryButton, self).__init__(**kwargs)
		self.size_hint = None, None
		self.width = 400
		self.height = 100
		self.center_x = 400
		self.font_size = 30
		self.background_color = (0/255, 109/255, 170/255, 1)
