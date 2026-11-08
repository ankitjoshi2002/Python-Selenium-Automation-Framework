import configparser
from pathlib import Path

_config = configparser.ConfigParser()
_config.read(Path(__file__).resolve().parent.parent / "config.ini")


def get(section, key):
    return _config[section][key]