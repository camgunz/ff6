import struct

from patch import Patch

class ROM:

    def __init__(self, data):
        self.data = data
        self.header_size = len(self.data) % 1024
        if self.header_size == 0:
            self.has_header = False
        elif self.header_size == 512:
            self.has_header = True
        else:
            raise Exception('Invalid header size %s' % (self.header_size))

    @staticmethod
    def from_file(file_name):
        with open(file_name, 'rb') as fobj:
            return ROM(bytearray(fobj.read()))

    def apply_ips_patch(self, patch):
        if patch.header:
            self.ensure_has_header()
        for command, args in patch:
            if command == 'patch':
                loc, patch_size, replacement_data = args
                self.data[loc:loc+patch_size] = replacement_data
            elif command == 'rle':
                loc, run_size, fill_byte = args
                self.data[loc:loc+run_size] = fill_byte * run_size
            elif command == 'truncate':
                truncate = args[0]
                self.data = self.data[:truncate]
            else:
                raise Exception('Unknown patch command "{}"'.format(command))
        if patch.header:
            self.ensure_has_no_header()

    def ensure_has_no_header(self):
        if self.has_header:
            del self.data[:self.header_size]
            self.header_size = 0
            self.has_header = False

    def ensure_has_header(self):
        if not self.has_header:
            self.data = bytearray((0,) * 512) + self.data
            self.header_size = 512
            self.has_header = True

    def save_to_file(self, file_name):
        with open(file_name, 'wb') as fobj:
            fobj.write(self.data)

def test():
    rom = ROM.from_file('Final Fantasy III (U) (V1.0) [!].smc')
    print(rom.has_header)
    rom.ensure_has_header()
    print('Has header: {} ({} bytes)'.format(rom.has_header, rom.header_size))
    rom.ensure_has_no_header()
    print('Has header: {} ({} bytes)'.format(rom.has_header, rom.header_size))
    rom.ensure_has_header()
    print('Has header: {} ({} bytes)'.format(rom.has_header, rom.header_size))
    rom.ensure_has_no_header()
    print('Has header: {} ({} bytes)'.format(rom.has_header, rom.header_size))
    rom.apply_ips_patch_file('five-digit-damage-improvement-nh10.ips')
    rom.save_to_file('five-digit-damage-improvement-nh10-py.smc')

if __name__ == '__main__':
    test()

# vi: et sw=4 ts=4 tw=79
