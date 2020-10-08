import kivy
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

kivy.require("1.9.1")


class StartScreen(FloatLayout):
	def __init__(self, **kwargs):
		super(StartScreen, self).__init__(**kwargs)
		self.orientation = "vertical"

		title = Label()
		title.text = "Probabilities Calculator"
		title.size_hint = None, None
		title.height = 100
		title.width = 200
		title.pos_hint = {"x": 0.3, "y": 0.8}

		self.add_widget(title)