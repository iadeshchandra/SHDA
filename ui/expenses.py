import json
from kivy.uix.screenmanager import Screen
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from core.database import Database

db = Database()

class Expenses(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical")

        self.category = Spinner(text="Category", values=["Social","Festival"])
        self.name = TextInput(hint_text="Name")
        self.total = TextInput(hint_text="Total")

        btn = Button(text="Add Expense")
        btn.bind(on_press=self.add)

        layout.add_widget(self.category)
        layout.add_widget(self.name)
        layout.add_widget(self.total)
        layout.add_widget(btn)

        self.add_widget(layout)

    def add(self, instance):
        items = json.dumps([{"name": self.name.text, "price": float(self.total.text)}])
        db.add_expense(self.category.text, self.name.text, items, float(self.total.text))