import imp


import kivy
import random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

red = [1,0,0,1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]

class MainApp(App):
    def build(self):
        # label = Label(text='Hello from Hoang',
        #     size_hint=(.5, .5),
        #     pos_hint={'center_x': .5, 'center_y': .5})

        # img = Image(source='D://documentations//ab.png',
        #     size_hint=(.5, .5),
        #     pos_hint={'center_x': .5, 'center_y': .5})

        layout = BoxLayout(padding=10)
        colors = [red, green, blue, purple]

        # for i in range(5):
        #     btn = Button(text="Button #%s" % (i+1),
        #                 background_color=random.choice(colors))

        #     layout.add_widget(btn)
        btn = Button(text="Button",
                        background_color=red)
        layout.add_widget(btn)
        return layout

if __name__ == '__main__':
    app = MainApp()
    app.run()