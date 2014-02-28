__author__ = 'JiNooNi'

FAKEGIR_PATH = "C:\\Users\\JiNooNi\\.cache\\fakegir"

import sys

def realign_fakegir_path():
    for path in sys.path:
        if path == FAKEGIR_PATH:
            sys.path.remove(path)
            sys.path.append(path)

            break