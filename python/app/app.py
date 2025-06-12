from typing import Any
import toml
import os
import subprocess
from python.plst import PlayListHandler

class App:
    def __init__(self) -> None:
        self._config = self.get_config()
        self._handler = PlayListHandler(self._config)

    def get_config(self) -> dict[str, Any]:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(os.path.dirname(current_dir))

        main_path = os.path.join(project_root, 'config', 'config.toml')
        secrets_path = os.path.join(project_root, 'config', 'secret.toml')
        secrets_path = os.path.join(project_root, secrets_path)

        base_config = toml.load(os.path.join(project_root, main_path))['playlist']
        secrets_config = {}
        if os.path.exists(secrets_path):
            secrets_config = toml.load(secrets_path)['playlist']
        for key, val in secrets_config.items():
            if isinstance(val, list) and isinstance(base_config[key], list):
                base_config[key] += val
            else:
                base_config[key] = val

        return base_config

    def make_plst(self) -> None:
        self._handler.upload_plst()

    def get_last(self) -> str | bytes:
        return os.path.join(self._config['playListsPath'], self._handler.lastPlst)

    def update_current(self) -> None:
        process = subprocess.Popen([self._config['foobarPath'], self.get_last()])
        try:
            process.wait(timeout=self._config['delay'])
        except subprocess.TimeoutExpired:
            process.terminate()
            process.kill()

