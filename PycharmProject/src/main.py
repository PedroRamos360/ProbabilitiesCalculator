import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout

from src import colors
from src.widgets.primary_button import PrimaryButton

kivy.require("1.9.1")


class ArrengementsScreen(FloatLayout):
	pass


class StartScreen(FloatLayout):
	@staticmethod
	def on_button1_pressed():
		window.root_window.remove_widget(window.root)
		window.root_window.add_widget(ArrengementsScreen())


class ProbabilitiesCalculatorApp(App):
	def build(self):
		return StartScreen()


Window.clearcolor = colors.background_color

window = ProbabilitiesCalculatorApp()
window.run()
