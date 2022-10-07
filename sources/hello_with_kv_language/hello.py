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



class ButtonApp(App):
    def build(self):
        return Button()

    def on_press_button(self):
        print('You press the button!')


if __name__ == '__main__':
    app = ButtonApp()
    app.run()
    