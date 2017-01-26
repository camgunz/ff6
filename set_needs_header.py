import os
import lib
import sys
import shutil

def main():
    if not len(sys.argv) == 2:
        sys.stderr.write('Must specify name of patch\n\n')
        os.exit(-2)
    config = lib.get_config()
    old_patch_name = sys.argv[1]
    new_patch_name = old_patch_name.replace('-nh10.ips', '-h10.ips')
    old_patch_path = os.path.join(config['patch_dir'], old_patch_name)
    new_patch_path = os.path.join(config['patch_dir'], new_patch_name)
    shutil.move(old_patch_path, new_patch_path)
    with open(config['patch_list'], 'r') as fobj:
        old_patch_list_data = fobj.read()
    new_patch_list_data = old_patch_list_data.replace(
        old_patch_name,
        new_patch_name
    )
    with open(config['patch_list'], 'w') as fobj:
        fobj.write(new_patch_list_data)

main()
