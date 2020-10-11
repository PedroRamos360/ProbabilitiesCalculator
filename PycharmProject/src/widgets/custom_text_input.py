import kivy
from kivy.uix.textinput import TextInput

kivy.require("1.9.1")


class CustomTextInput(TextInput):
	def __init__(self, **kwargs):
		super(CustomTextInput, self).__init__(**kwargs)
		self.size_hint = None, None
		self.width = 50
		self.height = 50
		self.center_y = 300
		self.multiline = False
		self.input_filter = "int"
