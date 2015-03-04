import kivy
kivy.require('1.8.0')

from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')

from kivy.app import App


class CalendarApp(App):
    """Basic App to hold the calendar widget."""

    def build(self):
        return self.root
