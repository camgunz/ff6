import struct

from ff6.dte import DTE_BATTLE
from ff6.patch import Patch

def _8bit_signed(num):
    if num < 8:
        return num
    if num == 8:
        return 0
    if num > 7:
        return -(num % 8)

class ROM:

    def __init__(self, data):
        self.data = bytearray(data)
        self.header_size = len(self.data) % 1024
        if self.header_size == 0:
            self.has_header = False
        elif self.header_size == 512:
            self.has_header = True
        else:
            raise Exception('Invalid header size %s' % (self.header_size))
        self.ensure_has_header()

    @classmethod
    def from_file(cls, file_name):
        with open(file_name, 'rb') as fobj:
            return cls(fobj.read())

    def apply_patch(self, patch):
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

    def read_byte(self, location):
        return struct.unpack_from('B', self.data, location)[0]

    def read_nybbles(self, location):
        byte = struct.unpack_from('B', self.data, location)[0]
        return (((byte & 0xF0) >> 4), (byte & 0x0F))

    def read_signed_nybbles(self, location):
        byte = struct.unpack_from('B', self.data, location)[0]
        return (_8bit_signed((byte & 0xF0) >> 4), _8bit_signed(byte & 0x0F))

    def read_low_bits(self, location, bit_count):
        assert bit_count > 0
        mask = (1 << bit_count) - 1
        byte = struct.unpack_from('B', self.data, location)[0]
        return byte & mask

    def read_high_bits(self, location, bit_count):
        assert bit_count > 0
        mask = (255 >> bit_count)
        byte = struct.unpack_from('B', self.data, location)[0]
        return (byte & mask) >> (8 - bit_count)

    def read_bit(self, location, bit_index):
        assert bit_index >= 0
        mask = 1 << (bit_index - 1)
        byte = struct.unpack_from('B', self.data, location)[0]
        return (byte & mask) and True or False

    def read_5_and_3_bits(self, location):
        byte = struct.unpack_from('B', self.data, location)[0]
        return (((byte & 0x1F) >> 5), (byte & 0x07))

    def read_short(self, location):
        return struct.unpack_from('<H', self.data, location)[0]

    def read_bytes(data, location, size):
        return struct.unpack_from('%ds' % (size), self.data, location)[0]

    def read_string(self, location, size):
        return struct.unpack_from('%ds' % (size), self.data, location)[0].decode('ascii')

    def read_dte_battle_string(self, location, size):
        dte_battle_indices = struct.unpack_from('%ds' % (size),
                                                self.data,
                                                location)[0]
        return ''.join([DTE_BATTLE[index] for index in dte_battle_indices])

