import kivy
from kivy.app import App
from kivy.core.window import Window
from src import colors

from src.screens.start_screen import StartScreen

kivy.require("1.9.1")


class ProbabilitiesCalculatorApp(App):
	def build(self):
		return StartScreen()


Window.clearcolor = colors.background_color

window = ProbabilitiesCalculatorApp()
window.run()
