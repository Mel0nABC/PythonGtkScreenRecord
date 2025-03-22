# importamos gi
import gi

# impotamos GTK4.0, se haría igual con otras librerias.
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


class DemoApplicationWindow(Gtk.ApplicationWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_title("Buenos días")

        self.entry = Gtk.Entry()
        self.entry.set_placeholder_text("Pon tu nombre.")
        self.entry.set_hexpand(True)
        self.entry.set_width_chars(10)

        self.button = Gtk.Button()
        self.button.set_label("Enviar")
        self.button.add_css_class("suggested-action")
        self.button.connect("clicked", self.on_saludame)

        self.display = Gtk.Label()
        self.display.set_label("Hola")

        horizontal = Gtk.Box()
        horizontal.set_orientation(Gtk.Orientation.HORIZONTAL)
        horizontal.set_spacing(10)
        horizontal.append(self.entry)
        horizontal.append(self.button)

        vertical = Gtk.Box()
        vertical.set_orientation(Gtk.Orientation.VERTICAL)
        vertical.set_spacing(10)
        vertical.set_margin_top(10)
        vertical.set_margin_bottom(10)
        vertical.set_margin_start(10)
        vertical.set_margin_end(10)
        vertical.append(horizontal)
        vertical.append(self.display)

        self.set_child(vertical)

        self.contador = 0

    def on_saludame(self, _):
        nombre = self.entry.get_text()
        saludo = f"Hola, {nombre}"
        self.display.set_label(saludo)


class DemoApplication(Gtk.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs, application_id="es.mel0n.Ejemplo")

    def do_activate(self):
        print("hola")
        win = DemoApplicationWindow(application=self)
        win.present()


app = DemoApplication()
app.run()


# https://www.youtube.com/live/9x1OfkVti2o?si=CreJ274wiLvhZ0BB
