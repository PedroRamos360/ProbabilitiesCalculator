import kivy
from kivy.app import App
from kivy.properties import ObjectProperty

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

import functions

from primary_button import PrimaryButton
from custom_label import CustomLabel
from custom_text_input import CustomTextInput
from back_button import BackButton
from calculate_button import CalculateButton
from title_label import Title
from result_output import ResultOutput

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
	calculation_result = Label(
		pos_hint={'center_x': 0.5, 'center_y': 0.15},
		color=(0, 0, 0, 1),
		font_name="RobotoMono-Regular",
		font_size=30
	)

	def on_calculate(self):
		try:
			result = functions.arrangements(int(self.elements_input.text), int(self.arrangements_input.text))
			if self.calculated:
				self.remove_widget(self.calculation_result)

			self.calculation_result.text = str(result)
			self.calculated = True

		except ValueError:
			if self.calculated:
				self.remove_widget(self.calculation_result)
			self.calculated = True
			self.calculation_result.text = "Try different values"
		finally:
			self.add_widget(self.calculation_result)


class CombinationsScreen(FloatLayout):
	elements_input = ObjectProperty(None)
	combinations_input = ObjectProperty(None)

	calculated = False
	calculation_result = Label(
		pos_hint={'center_x': 0.5, 'center_y': 0.15},
		color=(0, 0, 0, 1),
		font_name="RobotoMono-Regular",
		font_size=30
	)

	def on_calculate(self):
		try:
			result = functions.combinations(int(self.elements_input.text), int(self.combinations_input.text))
			if self.calculated:
				self.remove_widget(self.calculation_result)

			self.calculation_result.text = str(result)
			self.calculated = True
		except ValueError:
			if self.calculated:
				self.remove_widget(self.calculation_result)
			self.calculated = True
			self.calculation_result.text = "Try different values"
		finally:
			self.add_widget(self.calculation_result)


class PermutationsScreen(FloatLayout):
	elements_input = ObjectProperty(None)
	repetitions_input = ObjectProperty(None)

	calculated = False
	calculation_result = Label(
		pos_hint={'center_x': 0.5, 'center_y': 0.15},
		color=(0, 0, 0, 1),
		font_name="RobotoMono-Regular",
		font_size=30
	)

	def on_calculate(self):
		try:
			result = functions.permutations(int(self.elements_input.text), self.repetitions_input.text)
			if self.calculated:
				self.remove_widget(self.calculation_result)

			self.calculation_result.text = str(result)
			self.calculated = True
		except ValueError:
			if self.calculated:
				self.remove_widget(self.calculation_result)
			self.calculated = True
			self.calculation_result.text = "Try different values"
		finally:
			self.add_widget(self.calculation_result)


class ProbabilitiesCalculatorApp(App):
	@staticmethod
	def go_back():
		App.get_running_app().root.current = "StartScreen"

	def build(self):
		return RootWidget()


window = ProbabilitiesCalculatorApp()
window.run()
