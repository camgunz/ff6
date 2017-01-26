from configparser import ConfigParser

__CONFIG = None
__PROJECT_CONFIG_FILE_NAME = 'project.ini'

def get_config():
    global __CONFIG
    if __CONFIG is None:
        config = ConfigParser()
        config.read(__PROJECT_CONFIG_FILE_NAME)
        __CONFIG = {}
        for key in config['project']:
            __CONFIG[key] = config['project'][key]
    return __CONFIG
