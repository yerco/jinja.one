import yaml, os
from presentation.application import Application

def application(environ, start_response):
    application = Application()
    output = application.template.render(character="AxTp")
    
    status = '200 OK'
    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [bytes(output, 'utf-8')]
