from Main_screen import MainScreen
from Second_screen import SecondScreen

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

class liquidadorLaboral(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name = "main"))
        sm.add_widget(SecondScreen(name = "second"))
        return sm

if __name__ == "__main__":
    liquidadorLaboral().run()
