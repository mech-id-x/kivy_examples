from optparse import Values
from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp):

    data = {
        "Color Themes": "language-python",
        "C++": "language-cpp",
        "Ruby": "language-ruby",
        "Kivy": "language-kivy"
    }

    def callback(self, instance):
        """for keys,Values in data:
            if instance.icon == data(Values):
                lang = print("you pressed", instance.icon)
            else:
                pass"""

        if instance.icon == 'language-python':
            lang = "Python"
        elif instance.icon == 'language-cpp':
            lang = "C++"
        elif instance.icon == 'language-ruby':
            lang = "Ruby"
        elif instance.icon == 'language-kivy':
            lang = "Kivy"
        #self.root.ids.my_label.text = f'you pressed {lang}'

        #self.root.ids.my_label.text = f'you pressed {instance.icon}'

    def open(self):
        #self.root.ids.my_label.text = f'Open!'
        pass

    def close(self):
        #self.root.ids.my_label.text = f'Closed!'
        pass
    
    
    #every function on different label is executed with modules
    def execute(self):
        pass

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.primary_hue = "200"
        return Builder.load_file('default_app.kv')
    


""" "Red", "Pink", "Purple", "DeepPurple",
 "Indigo", "Blue", "LightBlue", "Cyan", "Teal",
  "Green", "LightGreen", "Lime", "Yellow", "Amber",
   "Organge", "DeepOrange", "Brown", "Gray", "BlueGray" """


MainApp().run()