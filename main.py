from kivy.app import App
from kivy.uix.label import Label

class TestApp(App):
    def build(self):
        return Label(text="Brahmastra Phase 1: Success!\nAb hum bade features jodenge.")

if __name__ == "__main__":
    TestApp().run()

