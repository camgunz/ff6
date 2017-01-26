from configparser import ConfigParser

__PROJECT_CONFIG_FILE_NAME = 'project.ini'
__CONFIG = None

def get_config():
    global __CONFIG
    if __CONFIG is None:
        config = ConfigParser()
        config.read(__PROJECT_CONFIG_FILE_NAME)
        __CONFIG = {}
        for key in config['project']:
            __CONFIG[key] = config['project'][key]
    return __CONFIG

# vi: et sw=4 ts=4 tw=79
