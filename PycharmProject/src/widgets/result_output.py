import kivy

from kivy.uix.boxlayout import BoxLayout

kivy.require('1.9.1')


class ResultOutput(BoxLayout):
	def __init__(self, **kwargs):
		super(ResultOutput, self).__init__(**kwargs)
		self.font_name = "RobotoMono-Regular"
		self.size_hint = 0.7, 0.12
		self.pos_hint = {'center_x': 0.5, 'center_y': 0.15}
		self.background_color = 1, 1, 1, 1
		self.font_size = 20
		self.width = 550
		self.height = 70
