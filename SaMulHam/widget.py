__author__ = 'JiNooNi'

from gi.repository import Gtk

class window(Gtk.Window):
    def __init__(self):
        self.connect("destroy", Gtk.main_quit)

    def start(self):
        Gtk.main()