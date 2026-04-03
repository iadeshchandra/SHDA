from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from core.database import Database
from services.firebase_service import push

db = Database()

class Members(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical")

        self.name = TextInput(hint_text="Name")
        self.phone = TextInput(hint_text="Phone")

        btn = Button(text="Add Member")
        btn.bind(on_press=self.add)

        layout.add_widget(self.name)
        layout.add_widget(self.phone)
        layout.add_widget(btn)

        self.add_widget(layout)

    def add(self, instance):
        db.add_member(self.name.text, self.phone.text)
        push("members", {"name": self.name.text})