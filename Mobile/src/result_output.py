import kivy

from kivy.uix.boxlayout import BoxLayout

kivy.require('1.9.1')


class ResultOutput(BoxLayout):
	def __init__(self, **kwargs):
		super(ResultOutput, self).__init__(**kwargs)
		self.font_name = "RobotoMono-Regular"
		self.size_hint = 0.9, 0.1
		self.pos_hint = {'center_x': 0.5, 'center_y': 0.15}
		self.background_color = 1, 1, 1, 1
