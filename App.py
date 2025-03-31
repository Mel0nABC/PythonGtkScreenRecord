from Controller import Controller
import gi

# impotamos GTK4.0, se haría igual con otras librerias.
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio, Gdk


class App(Gtk.Application):

    def __init__(self, **kwargs):
        super().__init__(**kwargs, application_id="es.mel0n.Ejemplo")

    def do_activate(self, **kwargs):
        settings = Gtk.Settings.get_default()
        builder = Gtk.Builder()
        builder.add_from_file("./ui/main.ui")
        window = builder.get_object("win")
        window.set_application(self)
        window.set_default_size(300, 400)
        control = Controller(builder)
        window.present()


apli = App()
apli.run()