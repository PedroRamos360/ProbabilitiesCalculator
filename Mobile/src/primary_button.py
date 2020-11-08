from kivymd.uix.button import MDRoundFlatButton


class PrimaryButton(MDRoundFlatButton):
	def __init__(self, **kwargs):
		super(PrimaryButton, self).__init__(**kwargs)
		self.font_name = "RobotoMono-Regular"
		self.size_hint = None, None
		self.font_size = 30
		self.text_color = (0, 0, 0, 1)
