import kivy
from kivy.uix.textinput import TextInput

kivy.require("1.9.1")


class CustomTextInput(TextInput):
	def __init__(self, **kwargs):
		super(CustomTextInput, self).__init__(**kwargs)
		self.size_hint = 0.3, 0.12
		self.font_size = 40
		self.padding = 15
		self.background_normal = ''
		self.background_color = 196/255, 196/255, 196/255, 1
		self.width = 300
		self.height = 80
		self.multiline = False
		self.input_filter = "int"
