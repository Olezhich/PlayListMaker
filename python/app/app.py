import toml
import os
from python.plst import plst_handler, PlayListHandler

class App:
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(os.path.dirname(current_dir))
        config_path = os.path.join(project_root, 'config', 'config.toml')
        self._config = toml.load(os.path.join(project_root, config_path))
        self._handler = PlayListHandler(self._config['playlist'])

    def make_plst(self):
        self._handler.upload_plst()

    def update_current(self):
        ...

