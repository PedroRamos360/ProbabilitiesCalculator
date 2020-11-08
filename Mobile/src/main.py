from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager

from primary_button import PrimaryButton
from title_label import Title


class RootWidget(ScreenManager):
	pass


class StartScreen(MDFloatLayout):
	@staticmethod
	def on_arrangements_pressed():
		MDApp.get_running_app().root.current = "ArrangementsScreen"

	@staticmethod
	def on_combinations_pressed():
		MDApp.get_running_app().root.current = "CombinationsScreen"

	@staticmethod
	def on_permutations_pressed():
		MDApp.get_running_app().root.current = "PermutationsScreen"


class ArrangementsScreen(MDFloatLayout):
	pass


class CombinationsScreen(MDFloatLayout):
	pass


class PermutationsScreen(MDFloatLayout):
	pass


class ProbabilitiesCalculator(MDApp):
	def build(self):
		return RootWidget()


ProbabilitiesCalculator().run()

