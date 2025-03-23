# importamos gi
import gi

# impotamos GTK4.0, se haría igual con otras librerias.
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio, Gdk


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
        # self.button.add_css_class("suggested-action")
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
        vertical.set_valign(Gtk.Align.CENTER)

        horizontal2 = Gtk.Box()
        horizontal2.set_orientation(Gtk.Orientation.HORIZONTAL)
        self.switch = Gtk.Switch()
        self.switch.connect("notify::active", self.on_switch)
        horizontal2.append(self.switch)

        vertical.append(horizontal)
        vertical.append(horizontal2)
        vertical.append(self.display)

        self.set_child(vertical)


        print(f"PRUEBAS ---> {self.get_modal()}")


    def on_saludame(self, _):
        nombre = self.entry.get_text()
        saludo = f"Hola, {nombre}"
        self.display.set_label(saludo)
        self.entry.set_text("")

    def on_switch(self, pspec, user_data):
        estado = self.switch.get_state()

        if estado:
            print("Activado")
            self.fullscreen()
            return

        print("Desactivado")
        self.unfullscreen()


class DemoApplication(Gtk.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs, application_id="es.mel0n.Ejemplo")

    def do_activate(self):
        settings = Gtk.Settings.get_default()
        # settings.set_property("gtk-theme-name", "Adwaita")
        # Modo oscuro de Adwait.
        settings.set_property("gtk-theme-name", "Adwaita-dark")
        win = DemoApplicationWindow(application=self)
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
            print(mon.get_subpixel_layout())


app = DemoApplication()
app.run()


# https://www.youtube.com/live/9x1OfkVti2o?si=CreJ274wiLvhZ0BB
