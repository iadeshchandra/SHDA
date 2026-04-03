from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from core.auth import Auth

auth = Auth()

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        auth.create_admin()

        layout = BoxLayout(orientation="vertical")

        self.u = TextInput(hint_text="Username")
        self.p = TextInput(hint_text="Password", password=True)

        btn = Button(text="Login")
        btn.bind(on_press=self.login)

        layout.add_widget(self.u)
        layout.add_widget(self.p)
        layout.add_widget(btn)

        self.add_widget(layout)

    def login(self, instance):
        if auth.login(self.u.text, self.p.text):
            self.manager.current = "dashboard"