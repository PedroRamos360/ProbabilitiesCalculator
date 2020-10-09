import kivy
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

from src import colors
from src.widgets.primary_button import PrimaryButton
from src.screens.arrengements_screen import ArrengementsScreen

kivy.require("1.9.1")


class StartScreen(FloatLayout):
	# @staticmethod
	# def on_press_button(self):
	# 	window.root_window.remove_widget(window.root)
	# 	window.root_window.add_widget(ArrengementsScreen())

	def __init__(self, **kwargs):
		super(StartScreen, self).__init__(**kwargs)
		self.orientation = "vertical"

		title = Label()
		title.size_hint = None, None
		title.font_size = 50
		title.width = 200
		title.height = 50
		title.center_x = 400
		title.center_y = 520
		title.text = "Probabilities Calculator"
		title.color = colors.white

		button1 = PrimaryButton()
		button1.center_y = 400
		button1.text = "Arrangements"

		button2 = PrimaryButton()
		button2.center_y = 280
		button2.text = "Combinations"

		button3 = PrimaryButton()
		button3.center_y = 160
		button3.text = "Permutations"

		self.add_widget(title)
		self.add_widget(button1)
		self.add_widget(button2)
		self.add_widget(button3)