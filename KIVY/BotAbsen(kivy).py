import kivy
from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label

class Myapp(App):
    def build(self):
        return Label(text='Halo Dunia Tipu Tipu', font_size=50)

if __name__ == '__main__':
    Myapp().run()