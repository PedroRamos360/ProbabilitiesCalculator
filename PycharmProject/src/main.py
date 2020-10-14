import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.properties import ObjectProperty

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

from backend import math

from widgets.primary_button import PrimaryButton
from widgets.custom_label import CustomLabel
from widgets.custom_text_input import CustomTextInput
from widgets.back_button import BackButton
from widgets.calculate_button import CalculateButton

kivy.require("1.9.1")


class RootWidget(ScreenManager):
	pass


class StartScreen(FloatLayout):
	@staticmethod
	def on_arrangements_pressed():
		App.get_running_app().root.current = "ArrangementsScreen"

	@staticmethod
	def on_combinations_pressed():
		App.get_running_app().root.current = "CombinationsScreen"

	@staticmethod
	def on_permutations_pressed():
		App.get_running_app().root.current = "PermutationsScreen"


class ArrangementsScreen(FloatLayout):
	elements_input = ObjectProperty(None)
	arrangements_input = ObjectProperty(None)

	calculated = False
	calculation_result = None

	def on_calculate(self):
		try:
			result = math.arrangements(int(self.elements_input.text), int(self.arrangements_input.text))
			if self.calculated:
				self.remove_widget(self.calculation_result)

			self.calculation_result = Label(text=str(result))
			self.add_widget(self.calculation_result)
			self.calculated = True

		except ValueError:
			if self.calculated:
				self.remove_widget(self.calculation_result)
			self.calculated = True
			self.calculation_result = Label(text="Try different values", center_x=100)
			self.add_widget(self.calculation_result)


class CombinationsScreen(FloatLayout):
	elements_input = ObjectProperty(None)
	combinations_input = ObjectProperty(None)

	calculated = False
	calculation_result = None

	def on_calculate(self):
		try:
			result = math.combinations(int(self.elements_input.text), int(self.combinations_input.text))
			if not self.calculated:
				self.calculation_result = Label(text=str(result))
				self.add_widget(self.calculation_result)
				self.calculated = True
			else:
				self.remove_widget(self.calculation_result)
				self.calculation_result = Label(text=str(result))
				self.add_widget(self.calculation_result)
		except ValueError:
			if self.calculated:
				self.remove_widget(self.calculation_result)
			self.calculated = True
			self.calculation_result = Label(text="Try different values", center_x=100)
			self.add_widget(self.calculation_result)


class PermutationsScreen(FloatLayout):
	elements_input = ObjectProperty(None)
	repetitions_input = ObjectProperty(None)

	calculated = False
	calculation_result = None

	def on_calculate(self):
		try:
			result = math.permutations(int(self.elements_input.text), self.repetitions_input.text)
			if not self.calculated:
				self.calculation_result = Label(text=str(result))
				self.add_widget(self.calculation_result)
				self.calculated = True
			else:
				self.remove_widget(self.calculation_result)
				self.calculation_result = Label(text=str(result))
				self.add_widget(self.calculation_result)
		except ValueError:
			if self.calculated:
				self.remove_widget(self.calculation_result)
			self.calculated = True
			self.calculation_result = Label(text="Try different values", center_x=100)
			self.add_widget(self.calculation_result)


class ProbabilitiesCalculatorApp(App):
	@staticmethod
	def go_back():
		App.get_running_app().root.current = "StartScreen"

	def build(self):
		return RootWidget()


Window.clearcolor = (185/255, 214/255, 170/242, 1)

window = ProbabilitiesCalculatorApp()
window.run()
