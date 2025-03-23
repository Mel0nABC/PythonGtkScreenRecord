import gi
import SubProcesos
import GestorFicheros

# impotamos GTK4.0, se haría igual con otras librerias.
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio, Gdk


class DemoApplicationWindow(Gtk.ApplicationWindow):

    recordStatus = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_title("Monitor recorder")

        verticalMain = Gtk.Box()
        verticalMain.set_orientation(Gtk.Orientation.VERTICAL)

        verticalMain.set_spacing(10)
        verticalMain.set_margin_top(10)
        verticalMain.set_margin_bottom(10)
        verticalMain.set_margin_start(10)
        verticalMain.set_margin_end(10)
        verticalMain.set_valign(Gtk.Align.CENTER)

        self.optionContainer = Gtk.Box()
        self.optionContainer.set_orientation(Gtk.Orientation.HORIZONTAL)
        self.optionContainer.set_halign(Gtk.Align.CENTER)
        self.recordLabel = Gtk.Label()
        self.recordLabel.set_label("RECORD")

        self.recordBtn = Gtk.Button()
        self.recordBtn.set_label("START")
        self.recordBtn.connect("clicked", self.start_stop_record)

        self.optionContainer.append(self.recordLabel)
        self.optionContainer.append(self.recordBtn)

        verticalMain.append(self.optionContainer)

        # horizontal = Gtk.Box()
        # horizontal.set_orientation(Gtk.Orientation.HORIZONTAL)
        # horizontal.set_spacing(10)

        # horizontal2 = Gtk.Box()
        # horizontal2.set_orientation(Gtk.Orientation.HORIZONTAL)
        # self.switchLabel = Gtk.Label()
        # self.switchLabel.set_label("FULLSCREEN")
        # self.switch = Gtk.Switch()
        # self.switch.connect("notify::active", self.on_switch)
        # horizontal2.append(self.switchLabel)
        # horizontal2.append(self.switch)

        # vertical.append(horizontal)
        # vertical.append(horizontal2)

        self.set_child(verticalMain)

    def on_saludame(self, _):
        nombre = self.entry.get_text()
        saludo = f"Hola, {nombre}"
        self.display.set_label(saludo)
        self.entry.set_text("")

    def on_switch(self, pspec, user_data):
        estado = self.switch.get_state()

        if estado:
            print("Activado")
            # self.fullscreen()
            self.fullscreen()
            return

        print("Desactivado")
        self.unfullscreen()

    def start_stop_record(self, _):
        btnStatus = self.recordBtn.get_label()
        if btnStatus.__eq__("START"):
            newFileName = GestorFicheros.get_file_name()
            self.recordStatus = SubProcesos.record_on_popen(GestorFicheros.get_file_name())
            self.recordBtn.set_label("STOP")
            self.on_record()
        else:
            if self.recordStatus:
                self.recordStatus.terminate()
                # GestorFicheros.finish_record_rename_file()
            self.recordBtn.set_label("START")

    def on_record(self, **kwargs):
        self.minimize()