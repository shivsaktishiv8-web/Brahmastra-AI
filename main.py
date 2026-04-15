from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

# Panini Logic: Rules-based language processing base
class PaniniEngine:
    def process_input(self, text, lang_pref):
        # Yahan offline logic aayega jo user ki local language samjhega
        if "profit" in text.lower():
            return "Trading Mode: Analyzing Market Offline..."
        return f"Brahmastra AI ({lang_pref}): Aapne kaha - {text}"

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.output = Label(text="Brahmastra AI: Ready (Offline)", size_hint_y=0.2)
        layout.add(self.output)
        
        self.input_text = TextInput(hint_text="Kuch bhi puche (Trading, Love, Code...)", multiline=False)
        layout.add(self.input_text)
        
        btn = Button(text="Execute Brahmastra", size_hint_y=0.2, background_color=(1, 0, 0, 1))
        btn.bind(on_press=self.run_logic)
        layout.add(btn)
        
        self.add_widget(layout)

    def run_logic(self, instance):
        engine = PaniniEngine()
        res = engine.process_input(self.input_text.text, "Mix/Local")
        self.output.text = res

class BrahmastraApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        return sm

if __name__ == "__main__":
    BrahmastraApp().run()
