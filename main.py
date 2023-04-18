from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp


class PruebaPantalla(MDBoxLayout):pass  
KV = '''
PruebaPantalla:
    orientation: 'horizontal'
    Screen:

        MDIconButton:
            icon: "language-python"
            pos_hint: {"center_x": .5, "center_y": .5}
            icon_size: "64sp"
            md_bg_color: [.97,.58,.1,1]
'''


class Main(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        return Builder.load_string(KV)
 
Main().run()