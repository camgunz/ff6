import csv

from configparser import ConfigParser

__PROJECT_CONFIG_FILE_NAME = 'project.ini'
__CONFIG = None
__PATCH_LIST = None

def get_patch_list():
    global __PATCH_LIST
    if __PATCH_LIST is None:
        config = get_config()
        patch_list_file_name = config['patch_list']
        patch_list = []
        with open(patch_list_file_name, 'r') as csv_fobj:
            for row in csv.DictReader(csv_fobj):
                patch_list.append((
                    row['file_name'],
                    row['header'] == 'y',
                    row['apply'] == 'y'
                ))
        __PATCH_LIST = patch_list
    return __PATCH_LIST

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
