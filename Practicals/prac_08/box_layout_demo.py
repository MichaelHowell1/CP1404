"""
CP1404 Prac 8 - Box Layout Demo
Class for BoxLayoutDemo for Kivy app
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Kivy App to demo box layout"""

    def build(self):
        """Build BoxLayout Demo Kivy app"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle greeting with user's name (input)"""
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def handle_clear(self):
        """Handle clearing of gui to blank"""
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = ''
        return self.root


BoxLayoutDemo().run()
