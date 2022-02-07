from presentation.application import Application
from business.error_handler import ErrorHandler

def application(environ, start_response):
    try:
        application = Application()
        output = application.render(character="Olafo", another="Otro")
    except Exception as e:
        error_handler = ErrorHandler()
        output = error_handler.error_message()
    status = '200 OK'
    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [bytes(output, 'utf-8')]
