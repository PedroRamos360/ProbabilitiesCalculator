import kivy
from kivy.uix.label import Label

kivy.require("1.9.1")


class Title(Label):
	def __init__(self, **kwargs):
		super(Title, self).__init__(**kwargs)
		self.font_name = "RobotoMono-Regular"
		self.font_size = 60
		self.width = 30
		self.pos_hint = {'center_x': 0.5, 'center_y': 0.85}
		self.color = 55.0/255, 57.0/255, 58.0/255, 1
