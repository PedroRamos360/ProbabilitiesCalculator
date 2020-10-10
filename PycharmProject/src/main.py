import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.label import Label

from src import colors
from src.backend import math

kivy.require("1.9.1")


class ArrangementsScreen(FloatLayout):
	elements_input = ObjectProperty(None)
	arrangements_input = ObjectProperty(None)

	calculated = False
	calculation_result = None

	def on_calculate(self):
		result = math.arrengements(int(self.elements_input.text), int(self.arrangements_input.text))

		if not self.calculated:
			self.calculation_result = Label(text=str(result))
			self.add_widget(self.calculation_result)
			self.calculated = True
		else:
			self.remove_widget(self.calculation_result)
			self.calculation_result = Label(text=str(result))
			self.add_widget(self.calculation_result)


class StartScreen(FloatLayout):
	@staticmethod
	def on_button1_pressed():
		window.root_window.remove_widget(window.root)
		window.root_window.add_widget(ArrangementsScreen())


class ProbabilitiesCalculatorApp(App):
	def build(self):
		return StartScreen()


Window.clearcolor = colors.background_color

window = ProbabilitiesCalculatorApp()
window.run()
