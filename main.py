from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from ui.login_screen import LoginScreen
from ui.dashboard import Dashboard
from ui.members import Members
from ui.donations import Donations
from ui.expenses import Expenses
from ui.reports import Reports

class SHDAApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(Dashboard(name="dashboard"))
        sm.add_widget(Members(name="members"))
        sm.add_widget(Donations(name="donations"))
        sm.add_widget(Expenses(name="expenses"))
        sm.add_widget(Reports(name="reports"))
        return sm

SHDAApp().run()
