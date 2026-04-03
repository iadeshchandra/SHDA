from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from services.pdf_service import create_report

class Reports(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical")

        btn = Button(text="Generate Report")
        btn.bind(on_press=self.gen)

        layout.add_widget(btn)
        self.add_widget(layout)

    def gen(self, instance):
        data = [["SHDA Report"],["Generated"]]
        create_report(data)