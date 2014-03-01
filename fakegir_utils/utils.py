__author__ = 'JiNooNi'

WIN32_FAKEGIR_PATH = "C:\\Users\\JiNooNi\\.cache\\fakegir"
LINUX_FAKEGIR_PATH = "/home/kri/.cache/fakegir"

import sys

def realign_fakegir_path():
    for path in sys.path:
        if path == WIN32_FAKEGIR_PATH or path == LINUX_FAKEGIR_PATH:
            sys.path.remove(path)
            sys.path.append(path)

            break