from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class TestKivy(App):
    def build(self):
        return Builder.load_file('testkivy.kv')

if __name__ == '__main__':
    TestKivy().run()