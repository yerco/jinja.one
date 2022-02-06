from jinja2 import Environment, FileSystemLoader, TemplateNotFound
import os
from jinja2 import Template

def application(environ, start_response):
    status = '200 OK'
    
    file_loader = FileSystemLoader('/var/www/jinja.one/templates/')
    template_name = 'hello_world.txt'
    env = Environment(loader=file_loader)
    template = env.get_template(template_name)
    output = template.render(character="Lautaro")

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    
    #print(output)
    return [bytes(output, 'utf-8')]
