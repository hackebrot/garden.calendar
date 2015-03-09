import kivy
kivy.require('1.8.0')

from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BoundedNumericProperty


class Week(BoxLayout):
    week_num = BoundedNumericProperty(1, min=1, max=53)


class CalendarApp(App):
    """Basic App to hold the calendar widget."""

    def build(self):
        for i in range(1, 54):
            self.root.ids.cal.add_widget(Week(week_num=i))
        return self.root
