fakegir_utils.realign_fakegir_path()

from gi.repository import Gtk, Gdk

window = Gtk.Window()
window.connect("destroy", Gtk.main_quit)

button = Gtk.Button()
button.set_label("Testing!")
window.add(button)

css_data = """
GtkWindow
{
        background-color: #000000;
}

GtkButton
{
        background-color: #00FF00;
}
"""

css_provider = Gtk.CssProvider()
css_provider.load_from_data(css_data)

screen = Gdk.Screen.get_default()

style_context = Gtk.StyleContext()
style_context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)

window.show_all()

Gtk.main()
