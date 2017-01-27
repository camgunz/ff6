import os
import lib
import rom

def main():
    config = lib.get_config()
    patch_list = lib.get_patch_list()
    ff3 = rom.ROM.from_file(config['base_rom'])
    n = 1
    for patch_file_name, requires_header, apply in lib.get_patch_list():
        if not apply:
            continue
        if requires_header:
            ff3.ensure_has_header()
        else:
            ff3.ensure_has_no_header()
        patch_file_path = os.path.join(config['patch_dir'], patch_file_name)
        print('Applying patch {} ({}/{})'.format(
            patch_file_name, n, len(patch_list),
        ))
        ff3.apply_ips_patch_file(patch_file_path)
        n += 1
    ff3.save_to_file(config['project_rom'])

main()

# vi: et sw=4 ts=4 tw=79
