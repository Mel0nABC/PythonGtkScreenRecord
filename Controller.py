import gi
import SubProcesos
import GestorFicheros

# impotamos GTK4.0, se haría igual con otras librerias.
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio, Gdk


class Controller:

    recordStatus = None
    builder = None
    screenSelected = None
    resolutionValue = None
    codecValue = None
    audioCheckStatus = False

    def __init__(self, builder):
        self.builder = builder
        self.recordBtn = builder.get_object("btnAction")

        self.dropScreen = self.builder.get_object("dropScreen")
        self.info_monitores()   
        self.dropResolution = self.builder.get_object("dropResolution")
        self.dropCodec = self.builder.get_object("dropCodec")

        self.ftsData = self.builder.get_object("ftsData")
        self.audioCheck = self.builder.get_object("audioCheck")

        self.recordBtn.connect("clicked", self.start_stop_record)

        self.dropScreen.connect("notify::selected", self.drop_down_change_value)
        self.dropResolution.connect("notify::selected", self.drop_down_change_value)
        self.dropCodec.connect("notify::selected", self.drop_down_change_value)

        self.audioCheck.connect("notify", self.checkbox_changed)



    def spin_changed(self, spin, data):
        print("Cambio")

    def checkbox_changed(self, checkbox, data):
        self.audioCheckStatus = checkbox.get_active()

    def drop_down_change_value(self, dropdown, pspec):

        self.dropDownValue = (
            dropdown.get_model().get_item(dropdown.get_selected()).get_string()
        )

        if dropdown == self.dropScreen:
            monitorDisplayPort = self.dropDownValue.split()[0]
            screenSelected = SubProcesos.get_monitor_id(monitorDisplayPort)
            print(screenSelected)

        if dropdown == self.dropResolution:
            self.resolutionValue = self.dropDownValue

        if dropdown == self.dropCodec:
            self.codecValue = self.dropDownValue

    def info_monitores(self):
        string_list = Gtk.StringList()
        self.dropScreen.props.model = string_list
        string_list.append("SELECCIONA UN MONITOR")
        display = Gdk.Display.get_default()
        monitores = display.get_monitors()
        for mon in monitores:
            string_list.append(
                f"{mon.get_connector()} - {mon.get_manufacturer()} - {mon.get_refresh_rate() / 1000}Hz"
            )

    def start_stop_record(self, _):
        btnStatus = self.recordBtn.get_label()
        if btnStatus.__eq__("START"):
            newFileName = GestorFicheros.get_file_name()
            self.recordStatus = SubProcesos.record_on_popen(
                GestorFicheros.get_file_name()
            )
            self.recordBtn.set_label("STOP")
            self.on_record()
        else:
            if self.recordStatus:
                self.recordStatus.terminate()
            self.recordBtn.set_label("START")

    def on_record(self, **kwargs):
        self.minimize()
