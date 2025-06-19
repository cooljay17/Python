#Converted the classic Temperature Converter CLI into a GUI tool
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

Window.size = (300, 150)

class TemperatureConverter(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        self.input_label = Label(text="Enter Temperature:")
        self.add_widget(self.input_label)

        self.input_text = TextInput(multiline=False)
        self.add_widget(self.input_text)

        self.button_layout = BoxLayout(orientation='horizontal', spacing=10)
        self.celsius_to_f_button = Button(text="Celsius to Fahrenheit")
        self.celsius_to_f_button.bind(on_press=self.celsius_to_f)
        self.button_layout.add_widget(self.celsius_to_f_button)

        self.f_to_celsius_button = Button(text="Fahrenheit to Celsius")
        self.f_to_celsius_button.bind(on_press=self.f_to_celsius)
        self.button_layout.add_widget(self.f_to_celsius_button)

        self.add_widget(self.button_layout)

        self.output_label = Label(text="Result:")
        self.add_widget(self.output_label)

        self.output_text = TextInput(multiline=False, readonly=True)
        self.add_widget(self.output_text)

    def celsius_to_f(self, instance):
        try:
            celsius = float(self.input_text.text)
            fahrenheit = (celsius * 9/5) + 32
            self.output_text.text = f"{fahrenheit:.2f} °F"
        except ValueError:
            self.output_text.text = "Invalid Input"

    def f_to_celsius(self, instance):
        try:
            fahrenheit = float(self.input_text.text)
            celsius = (fahrenheit - 32) * 5/9
            self.output_text.text = f"{celsius:.2f} °C"
        except ValueError:
            self.output_text.text = "Invalid Input"

class TemperatureConverterApp(App):
    def build(self):
        return TemperatureConverter()

if __name__ == '__main__':
    TemperatureConverterApp().run()