import kivy
from kivy.app import App
from kivy.core.window import Window

from screens.StartScreen import StartScreen

kivy.require("1.9.1")


class ProbabilitiesCalculatorApp(App):
	def build(self):
		return StartScreen()


Window.size = 400, 600


janela = ProbabilitiesCalculatorApp()
janela.run()
