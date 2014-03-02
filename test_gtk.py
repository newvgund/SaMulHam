__author__ = 'kri'

from fakegir import utils as fakegir_utils

fakegir_utils.realign_fakegir_path()

from system import io as io_utils

from gi.repository import Gtk, Gdk

# Create windows!
window = Gtk.Window()

text_view = Gtk.TextView()
text_view.set_editable(False)
io_buffer = text_view.get_buffer()

io_selector = io_utils.get_io_selector()
io_selector.add_output_stream( io_utils.GtkOutputBuffer( io_buffer ) )

window.add(text_view)

window.show_all()
window.connect("destroy", Gtk.main_quit)

# setting drag & drop.
# target - flags - id(Gdk.Atom / int / int)
drag_target_lists = [
    ('text/plain', 0, 0),
    ('TEXT', 0, 1),
    ('STRING', 0, 2),
    ('text/uri-list', 0, 3)
]
window.drag_dest_set(Gtk.DestDefaults.ALL, [], Gdk.DragAction.COPY)
window.drag_dest_set_target_list(drag_target_lists)

def drag_data_received(widget, drag_context, x, y, data, info, time):
    print("Hi!")

window.connect("drag-data-received", drag_data_received)

print("Haha!")

Gtk.main()