import os
import lib
import rom

STOP_AFTER_MIN_PATCH = False
STOP_BEFORE_FF3_PATCHES = False
STOP_AFTER_PATCH_COUNT = None

def main():
    config = lib.get_config()
    patch_list = lib.get_patch_list()
    ff3 = rom.ROM.from_file(config['base_rom'])
    n = 1
    for patch_file_name, requires_header, apply in lib.get_patch_list():
        if STOP_BEFORE_FF3_PATCHES:
            if patch_file_name == 'FF3-AnonymousAttack-N0.ips':
                break
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
        if STOP_AFTER_MIN_PATCH and patch_file_name == 'RefBeam.ips':
            break
        if STOP_AFTER_PATCH_COUNT and n == STOP_AFTER_PATCH_COUNT:
            break
    ff3.save_to_file(config['project_rom'])

main()

# vi: et sw=4 ts=4 tw=79
