""" config_manager module"""

from abc import ABC, abstractmethod
# from config_manager.consul import ConsulConfig
from config_manager.file_system import FileConfig


class ConfigHandler(ABC):
    """This is a class for configuration handler."""

    @abstractmethod
    def get_config_data(self, key):
        """abstract method for get_config_data"""
        raise NotImplementedError


# class ConsulConfigManager(ConfigHandler):
#
#     def __init__(self, host, port, consul_path):
#         # self.consul_config = ConsulConfig(host, port)
#         self.consul_path = consul_path

    # def get_config_data(self, key):
    #
    #     config_data = self.consul_config.get_config("{}{}".format(self.consul_path, key))
    #     if config_data is None:
    #         return False
    #     else:
    #         return config_data

class FileConfigManager(ConfigHandler):
    """ This is a class for file configuration manager."""

    def __init__(self, file_path):
        self.file_path = file_path
        self.file_configs = FileConfig(file_path)

    def get_config_data(self, key):
        """ GET method for get_config_data"""
        try:
            return self.file_configs.configs[key]
        except KeyError:
            return False
