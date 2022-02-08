import sys
from tokenize import String

class ErrorHandler():

    def __init__(self) -> None:
        self.output = ""

    def error_message(self) -> String:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        self.output += 'File:' + exc_traceback.tb_frame.f_code.co_filename + '<br>'
        self.output += 'Line Number: ' + str(exc_traceback.tb_lineno) + '<br>'
        self.output += 'Method Name: ' + exc_traceback.tb_frame.f_code.co_name + '<br>'
        self.output += 'Type: ' + exc_type.__name__ + '<br>'
        self.output += 'Message: ' + str(exc_value) + '<br>'
        return self.output