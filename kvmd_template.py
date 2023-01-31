from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"
		return Builder.load_file('alert.kv')


class MainApp(MDApp):

	data = {
		"language-python": "Python",
		"language-ruby": "Ruby",
		"language-javascript": "JS"
	}
	
	def callback(self, instance):
		if instance.icon == 'language-python':
			lang = "Python"
		elif instance.icon == 'language-javascript':
			lang = "JS"
		elif instance.icon == 'language-ruby':
			lang = "Ruby"

		self.root.ids.my_label.text = f'You Pressed {lang}'

	#Open
	def open(self):
		self.root.ids.my_label.text = f'Open!!'		

	# Close
	def close(self):
		self.root.ids.my_label.text = f'Close!!!'				

	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"
		return Builder.load_file('sd.kv')


#### Vstavljanje gumbov za ukaze v python skripti!
	def show_alert_dialog(self):
		if not self.dialog:
			self.dialog = MDDialog(
				title = "Pretty Neat, Right?!",
				text = "This is just some text that goes here...",
				buttons =[
					MDFlatButton(
						text="CANCEL", text_color=self.theme_cls.primary_color, on_release = self.close_dialog
						),
					MDRectangleFlatButton(
						text="Yes It's Neat!", text_color=self.theme_cls.primary_color, on_release = self.neat_dialog
						),
					],
				)

		self.dialog.open()
	
MainApp().run()