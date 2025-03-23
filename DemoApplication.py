import DemoApplicationWindow
import gi

# impotamos GTK4.0, se haría igual con otras librerias.
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio, Gdk


class DemoApplication(Gtk.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs, application_id="es.mel0n.Ejemplo")

    def do_activate(self, **kwargs):
        settings = Gtk.Settings.get_default()
        # settings.set_property("gtk-theme-name", "Adwaita")
        # Modo oscuro de Adwait.
        settings.set_property("gtk-theme-name", "Adwaita-dark")
        win = DemoApplicationWindow.DemoApplicationWindow(application=self)
        win.set_default_size(400, 300)
        win.present()
        self.info_monitores()
        # para hacer pruebas sin abrir gráficos.
        # win.close()

    def info_monitores(self):
        display = Gdk.Display.get_default()
        monitores = display.get_monitors()
        for mon in monitores:
            print(f"Marca: {mon.get_manufacturer()}")
            print(f"Modelo: {mon.get_model()}")
            print(f"Frecuencia: {mon.get_refresh_rate() / 1000} Hz")
