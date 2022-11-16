"""
CP1404 Prac 8 - Convert Miles Km
Class for MilesConverterApp for Kivy app
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

miles_to_km = 1.60934


class MilesConverterApp(App):
    """Kivy App to allow conversion from miles to kilometres"""
    output_km = StringProperty()

    def build(self):
        """Build the MilesConverterApp Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def validate_input(self):
        """Error check input, return 0 if invalid and float if valid"""
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0

    def handle_conversion(self, value):
        """Convert mile input into km and output to label"""
        value = self.validate_input()
        result = value * miles_to_km
        self.output_km = str(result)

    def handle_increment(self, change):
        """Handle incremental change from button up/down press"""
        value = self.validate_input() + change
        self.root.ids.input_number.text = str(value)


MilesConverterApp().run()
