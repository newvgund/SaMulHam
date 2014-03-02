import sys

"""
 - IOStreamSelector

 it will replace default python stdin / stdout / stderr to other class.

* replace default IO stream.
* toggleable io option & class.
"""

class Stream(file):
    pass

class InputStream(Stream):
    pass

class OutputStream(Stream):
    pass

class ErrorStream(Stream):
    pass

class IOStreamSelector(object):
    def __init__(self):
        self.__use_system_out_stream__ = True
        self.__system_out_stream__ = None

        self.__use_system_input_stream__ = True
        self.__system_input_stream__ = None

        self.__use_system_error_stream__ = True
        self.__system_error_stream__ = None

        self._input_router = []
        self._output_router = []
        self._error_router = []

    def replace_system_io(self):
        """
        replace system io to IOStreamSelector.
        """
        if sys.stdin != None:
            self.__system_input_stream__ = sys.stdin

        if sys.stdout != None:
            self.__system_out_stream__ = sys.stdout

        if sys.stderr != None:
            self.__system_error_stream__ = sys.stderr

        sys.stdin = self
        sys.stdout = self
        sys.stderr = self

    def add_output_stream(self, stream):
        if not isinstance( stream, OutputStream ):
            raise TypeError()

        self._output_router.append(stream)

    def readline(self):
        if self.__use_system_input_stream__:
            return self.__system_input_stream__.readline()

    def write(self, data):
        if self.__use_system_out_stream__:
            self.__system_out_stream__.write(data)

        for stream in self._output_router:
            if isinstance( stream, OutputStream ):
                stream.write(data)

__sys_io_selector__ = IOStreamSelector()
__sys_io_selector__.replace_system_io()

def get_io_selector():
    return __sys_io_selector__

class GtkOutputBuffer(OutputStream):
    def __init__(self, buffer):
        self.__buffer__ = buffer

    def write(self, data):
        self.__buffer__.insert(self.__buffer__.get_end_iter(), ''.join(data))