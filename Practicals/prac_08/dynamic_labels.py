"""
CP1404 Prac 8 - Dynamic labels
Class for DynamicLabelsApp for Kivy app
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Kivy App to dynamically create labels"""

    def __init__(self, **kwargs):
        """Build main app and store names"""
        super().__init__(**kwargs)
        self.names = ["Name1", "Name2", "Name3"]

    def build(self):
        """Build the DynamicLabelsApp class from the kv file with Kivy Gui"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from list and display in app"""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
