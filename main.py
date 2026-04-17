from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class BrahmastraApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        # Tera Vision: Panini Logic Base
        label = Label(
            text="🔱 BRAHMASTRA AI 🔱\nOffline & Panini Logic Enabled\nStatus: Initializing...",
            halign="center",
            font_size='20sp'
        )
        layout.add_widget(label)
        return layout

if __name__ == "__main__":
    BrahmastraApp().run()
