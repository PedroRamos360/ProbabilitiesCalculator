import kivy
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image

kivy.require("1.9.1")


class BackButton(ButtonBehavior, Image):
	def __init__(self, **kwargs):
		super(BackButton, self).__init__(**kwargs)
		self.source = "img/arrowback.jpg"
		self.size_hint = None, None

		self.font_size = 20
		self.width = 150
		self.height = 50
		self.pos_hint = {'center_x': 0.1, 'center_y': 0.84}


# Image:
#   source: 'kivy.png'
#   y: self.parent.y + self.parent.height - 200
#   x: self.parent.x
