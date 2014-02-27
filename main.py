__author__ = 'JiNooNi'

from lib.fakegir_utils import utils as fakegir_utils

fakegir_utils.realign_fakegir_path()

from lib.SaMulHam import widget

main_window = widget.window()
main_window.show_all()
main_window.start()