import struct

class ROM:

    IPS_HEADER_BYTES = tuple([ord(c) for c in 'PATCH'])
    IPS_EOF_BYTES = tuple([ord(c) for c in 'EOF'])

    def __init__(self, rom_data):
        self.rom_data = bytearray(rom_data)
        self.header_size = len(self.rom_data) % 1024
        if self.header_size == 0:
            self.has_header = False
        elif self.header_size == 512:
            self.has_header = True
        else:
            raise Exception('Invalid header size %s' % (self.header_size))

    @staticmethod
    def from_file(file_name):
        with open(file_name, 'rb') as fobj:
            return ROM(fobj.read())

    def apply_ips_patch(self, patch_data):
        offset = 0
        header = struct.unpack_from('5B', patch_data)
        offset += 5
        if header != self.IPS_HEADER_BYTES:
            raise Exception('Invalid IPS patch data')
        while offset < len(patch_data):
            start_offset = offset
            loc = struct.unpack_from('3B', patch_data, offset=offset)
            offset += 3
            if loc == self.IPS_EOF_BYTES:
                if len(patch_data) - offset == 3:
                    truncate = struct.unpack_from(
                        '3B',
                        patch_data,
                        offset=offset
                    )
                    offset += 3
                    truncate = (
                        (truncate[0] << 16) +
                        (truncate[1] << 8) +
                        (truncate)
                    )
                    self.rom_data = self.rom_data[:truncate]
                break
            loc = ((loc[0] << 16) + (loc[1] << 8)  + (loc[2]))
            patch_size = struct.unpack_from('!H', patch_data, offset=offset)
            offset += 2
            patch_size = patch_size[0]
            if patch_size == 0:
                run_size = struct.unpack_from('!H', patch_data, offset=offset)
                offset += 2
                run_size = run_size[0]
                fill_byte = struct.unpack_from('c', patch_data, offset=offset)
                offset += 1
                fill_byte = fill_byte[0]
                self.rom_data[loc:loc+run_size] = fill_byte * run_size
            else:
                replacement_data = struct.unpack_from(
                    '!{}s'.format(patch_size),
                    patch_data,
                    offset
                )
                offset += patch_size
                replacement_data = replacement_data[0]
                self.rom_data[loc:loc+patch_size] = replacement_data

    def apply_ips_patch_file(self, ips_patch_file_name):
        with open(ips_patch_file_name, 'rb') as fobj:
            self.apply_ips_patch(fobj.read())

    def ensure_has_no_header(self):
        if self.has_header:
            del self.rom_data[:self.header_size]
            self.header_size = 0
            self.has_header = False

    def ensure_has_header(self):
        if not self.has_header:
            self.rom_data = bytearray((0,) * 512) + self.rom_data
            self.header_size = 512
            self.has_header = True

    def save_to_file(self, file_name):
        with open(file_name, 'wb') as fobj:
            fobj.write(self.rom_data)

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
