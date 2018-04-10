from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder


class MilesToKilometres(App):
    """
    An app for converting miles to Kilometers.
    """

    def build(self):
        """
        """
        Window.size = (500, 250)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles_converter.kv')
        return self.root

    def handle_convert(self, miles):
        """
        """
        convert = miles * 1.609
        self.root.ids.kilometres_label.text = str(convert)

    def handle_increase(self, miles):
        """
        """
        plus_one = miles + 1
        self.root.ids.input_miles.text = plus_one

    def handle_decrease(self, miles):
        """
        """
        minus_one = miles - 1
        self.root.ids.input_miles.text = minus_one

MilesToKilometres().run()