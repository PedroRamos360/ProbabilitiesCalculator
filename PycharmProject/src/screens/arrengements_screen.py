import kivy
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

kivy.require("1.9.1")


class ArrengementsScreen(FloatLayout):
	def __init__(self, **kwargs):
		super(ArrengementsScreen, self).__init__(**kwargs)

		label = Label(text="Arrengements")

		self.add_widget(label)