__author__ = 'kri'

import os

CURRENT_WORKING_PATH = os.path.realpath(__file__)

DEFAULT_HOME_PATH = "/home/kri/"

DEFAULT_PLUGIN_PATH = "plugin/"
DEFAULT_SETTING_PATH = ".SaMulHam/"

DEFAULT_SETTING_FILE = ".config"
DEFAULT_PLUGIN_EXTENSION = ".exp"

"""
* Default program init cycle

1. run program.
2. read .setting file on ~/.SaMulHam/.setting
3. if exist .setting file, we'll open and setting data.
4. if not exist .setting file, we'll create .setting file and store default state. and re-open.
"""

def read_setting_file(path=None):
    """
    read_setting_file

    @param
    path


    """

    if path is not None:
        path = DEFAULT_SETTING_PATH

    default_setting_path = DEFAULT_HOME_PATH + path

    # first, we checked default directory.
    if not os.path.exists(default_setting_path):
        # we create default directory.
        try:
            os.makedirs(default_setting_path)
        except:
            print("Error! can't create any directory.")
        finally:
            pass

    default_setting_file = default_setting_path + DEFAULT_SETTING_FILE

    # second, we checked default setting file too.
    if not os.path.exists(default_setting_file):
        try:
            default_file = open(default_setting_file, mode="wt")
        except:
            default_file = None
        finally:
            if default_file is None:
                pass