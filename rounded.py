from kivy.properties import NumericProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout


class BorderDemo(BoxLayout):
    borderwidth = NumericProperty(1)
    corners = ListProperty([0, 0, 0, 0])
