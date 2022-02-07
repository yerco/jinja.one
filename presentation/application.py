from posixpath import abspath, dirname
from jinja2 import Environment, FileSystemLoader
import yaml
from os.path import dirname

class Application:

    def __init__(self) -> None:
        config_file = dirname(dirname(__file__)) + '/include/configs/config.yml'
        with open(config_file , 'r') as f:
            config = yaml.safe_load(f)

        self.template_name = config["TEMPLATES"]["INITIAL_TEMPLATE"]
        self.file_loader = FileSystemLoader(config["TEMPLATES"]["TEMPLATES_DIR"])
        self.env = Environment(loader=self.file_loader)
        self.template = self.env.get_template(self.template_name)
