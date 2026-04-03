from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class Dashboard(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical")

        for name in ["members","donations","expenses","reports"]:
            b = Button(text=name.capitalize())
            b.bind(on_press=lambda x, n=name: self.switch(n))
            layout.add_widget(b)

        self.add_widget(layout)

    def switch(self, screen):
        self.manager.current = screen