"""

"""
import os

import toml

# TODO: move to engine???
default_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "default.toml")


class Settings(dict):

    @classmethod
    def default(cls):
        return Settings.from_toml(default_path)

    @classmethod
    def from_toml(cls, file_name):
        data = toml.load(os.path.abspath(file_name))
        return cls().override(data)

    def __init__(self):
        super().__init__()
        self.__dict__ = self

    def override(self, data: dict):
        for key in data.keys():
            if key in self and isinstance(data[key], dict) and isinstance(self[key], dict):
                data[key] = {**self[key], **data[key]}
            self[key] = data[key]
        return self
