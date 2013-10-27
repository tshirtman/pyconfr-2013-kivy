from kivy.app import App
from kivy.core.window import Window
from kivy.properties import NumericProperty, StringProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivy.lang import Builder
from random import random
from math import pi

# needed for kv
from kivy.garden import magnet
#from kivy.garden.magnet import transitions

transitions = (
    'out_sine', 'out_quint', 'out_quart', 'out_quad', 'out_expo',
    'out_cubic', 'out_circ', 'out_bounce', 'out_back', 'linear',
    'in_sine', 'in_quint', 'in_quart', 'in_quad', 'in_out_sine',
    'in_out_quint', 'in_out_quart', 'in_out_quad', 'in_out_expo',
    'in_out_cubic', 'in_out_circ', 'in_out_bounce', 'in_out_back',
    'in_expo', 'in_cubic', 'in_circ', 'in_bounce', 'in_back',)


class PresApp(App):
    page = NumericProperty(0)
    colors = ListProperty([[random() for i in range(4)] for i in range(3)])
    origins = ListProperty([[random() * Window.width, random() * Window.height] for i in range(3)])
    angles = ListProperty([random() * 2 * pi for i in range(3)])

    def build(self):
        Window.bind(on_keyboard=self.manage_key)
        self.animate_bg()
        return super(PresApp, self).build()

    def animate_bg(self, *args):
        a = Animation(
                colors=[[random() for i in range(4)] for i in range(3)],
                origins=[[random() * Window.width, random() * Window.height] for i in range(3)],
                angles=[random() * 2 * pi for i in range(3)],
                d=60,
                t='in_out_cubic')
        a.bind(on_complete=self.animate_bg)
        a.start(self)

    def manage_key(self, window, key, *args):

        if key in (273, 276):
            self.page -= 1

        elif key in (274, 275):
            self.page += 1

        self.page %= len(self.root.ids.gl.children)

        print key

    def on_page(self, *args):
        print self.page

class PresWidget(BoxLayout):
    source = StringProperty('')

    def on_source(self, *args):
        if self.children:
            self.clear_widgets()

        w = Builder.load_string(self.source)
        if w:
            self.add_widget(w)

if __name__ == '__main__':
    PresApp().run()
