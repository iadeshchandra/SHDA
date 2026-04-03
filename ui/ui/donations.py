from kivy.uix.screenmanager import Screen
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from core.database import Database

db = Database()

class Donations(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical")

        members = db.get_members()
        values = [f"{m[0]} - {m[1]}" for m in members]

        self.member = Spinner(text="Select Member", values=values)
        self.amount = TextInput(hint_text="Amount")

        btn = Button(text="Add Donation")
        btn.bind(on_press=self.add)

        layout.add_widget(self.member)
        layout.add_widget(self.amount)
        layout.add_widget(btn)

        self.add_widget(layout)

    def add(self, instance):
        mid = int(self.member.text.split(" - ")[0])
        db.add_donation(mid, float(self.amount.text))