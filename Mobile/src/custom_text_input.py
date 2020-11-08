import kivy
from kivy.uix.textinput import TextInput

kivy.require("1.9.1")


class CustomTextInput(TextInput):
	def __init__(self, **kwargs):
		super(CustomTextInput, self).__init__(**kwargs)
		self.size_hint = None, None
		self.height = 100
		self.width = 400
		self.font_name = "RobotoMono-Regular"
		self.font_size = 40
		self.padding = 10, (self.height - 70)/2, 10, (self.height - 70)/2
		self.background_normal = ''
		self.background_color = 200.0/255, 200.0/255, 200.0/255, 1
		self.multiline = False
		self.input_filter = "int"
