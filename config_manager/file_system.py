"""file_system"""

from configparser import ConfigParser


class FileConfig:
    """This is a class for file_configuration."""

    def __init__(self, file_path):
        config_parser = ConfigParser()
        config_parser.read(file_path)
        self.configs = {s: dict(config_parser.items(s, True)) for s in config_parser.sections()}
