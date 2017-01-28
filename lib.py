import os
import csv

from configparser import ConfigParser

from rom import ROM
from patch import Patch

__PROJECT_CONFIG_FILE_NAME = 'project.ini'
__CONFIG = None
__PATCH_LIST = None

def build_rom(buf=None):
    config = get_config()
    patch_list = get_patch_list()
    ff3 = ROM.from_file(config['base_rom'])
    for n, patch in enumerate(get_patch_list()):
        if not patch.apply:
            continue
        print('Applying patch {} ({}/{})'.format(
            patch.file_name,
            n + 1,
            len(patch_list),
        ))
        ff3.apply_patch(patch)
    return ff3

def get_patch_list():
    global __PATCH_LIST
    if __PATCH_LIST is None:
        config = get_config()
        patch_list_file_name = config['patch_list']
        patch_list = []
        with open(patch_list_file_name, 'r') as csv_fobj:
            for row in csv.DictReader(csv_fobj):
                patch_list.append(Patch.from_file(
                    os.path.join(config['patch_dir'], row['file_name']),
                    row['header'] == 'y',
                    row['apply'] == 'y',
                    row['notes']
                ))
        __PATCH_LIST = patch_list
    return __PATCH_LIST

def save_patch_list():
    config = get_config()
    patch_list = get_patch_list()
    patch_list_file_name = config['patch_list']
    with open(patch_list_file_name, 'w', newline='') as csv_fobj:
        writer = csv.writer(csv_fobj)
        writer.writerow(('file_name', 'header', 'apply', 'notes'))
        for patch in patch_list:
            writer.writerow((
                patch.file_name,
                patch.header and 'y' or 'n',
                patch.apply and 'y' or 'n',
                patch.notes
            ))

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
