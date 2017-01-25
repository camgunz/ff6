from configparser import ConfigParser

__CONFIG = None
__PROJECT_CONFIG_FILE_NAME = 'project.ini'

def main():
    config = ConfigParser()
    config.read('project.ini')
    for key in config['project']:
        print('{}: {}'.format(key, config['project'][key]))

