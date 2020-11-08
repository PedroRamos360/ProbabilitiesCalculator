from kivymd.uix.label import MDLabel


class Title(MDLabel):
	def __init__(self, **kwargs):
		super(Title, self).__init__(**kwargs)
		self.halign = 'center'
		self.font_style = 'H4'
		self.font_name = "RobotoMono-Regular.ttf"
		self.color = 1, 1, 1, 1
		self.pos_hint = {"center_y": 0.85}
