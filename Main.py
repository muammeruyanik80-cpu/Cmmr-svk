from kivy.app import App
from kivy.uix.label import Label

class CmmrApp(App):
    def build(self):
        return Label(text="Cmmr Stok Takip Uygulaması")

if __name__ == "__main__":
    CmmrApp().run()
