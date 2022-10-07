from cProfile import label
import imp
from re import T


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
        label_test = False
        img_test = False
        boxlayout = False
        event_test = True

        if label_test:
            label = Label(text='Hello from Hoang',
                size_hint=(.5, .5),
                pos_hint={'center_x': .5, 'center_y': .5})
            return label

        #------------------------------------------------#
        if img_test:
            img = Image(source='D://documentations//ab.png',
                size_hint=(.5, .5),
                pos_hint={'center_x': .5, 'center_y': .5})
            return img

        #------------------------------------------------#
        if boxlayout:
            layout = BoxLayout(padding=100, spacing=50)
            colors = [red, green, blue, purple]

            for i in range(5):
                btn = Button(text="Button #%s" % (i+1),
                            background_color=random.choice(colors))

                layout.add_widget(btn)
            return layout

        #------------------------------------------------#
        if event_test:
            bt = Button(text='Hoang Button',
                size_hint=(.5, .5),
                pos_hint={'center_x': .5, 'center_y': .5})
            bt.bind(on_press=self.on_press_button)
            print("my current state is {}".format(bt.state))
            return bt
    
    def on_press_button(self, instance):
        print('The button <%s> is being pressed' % instance.text)
        print("my current state is {}".format(instance.state))

if __name__ == '__main__':
    app = MainApp()
    app.run()