import struct

from ff6.dte import *
from ff6.patch import Patch

def _signed(num, bit_width):
    mask1 = (1 << bit_width) - 1
    mask2 = 1 << (bit_width - 1)
    num = num & mask1
    return num | (-(num & mask2))

def _unsigned(num, bit_width):
    return num & ((1 << bit_width) - 1)

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

    def __eq__(self, other):
        return self.data == other.data

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
        if not self.has_header:
            return
        del self.data[:self.header_size]
        self.header_size = 0
        self.has_header = False

    def ensure_has_header(self):
        if self.has_header:
            return
        self.data = bytearray((0,) * 512) + self.data
        self.header_size = 512
        self.has_header = True

    def save_to_file(self, file_name):
        with open(file_name, 'wb') as fobj:
            fobj.write(self.data)

    def read_byte(self, location):
        return struct.unpack_from('B', self.data, location)[0]

    def write_byte(self, location, byte):
        struct.pack_into('B', self.data, location, byte)

    def read_low_bits(self, location, bit_width):
        assert bit_width > 0
        assert bit_width < 8
        mask = (1 << bit_width) - 1
        byte = self.read_byte(location)
        return byte & mask

    def read_low_signed_bits(self, location, bit_width):
        assert bit_width > 0
        assert bit_width < 8
        mask = (1 << bit_width) - 1
        byte = self.read_byte(location)
        return _signed(byte & mask, bit_width)

    def write_low_bits(self, location, bit_width, low_bits):
        assert bit_width > 0
        assert bit_width < 8
        byte = self.read_byte(location)
        high_bits = self.read_high_bits(location, 8 - bit_width) << bit_width
        self.write_byte(location, high_bits | _unsigned(low_bits, bit_width))

    def read_high_bits(self, location, bit_width):
        assert bit_width > 0
        assert bit_width < 8
        mask = ((1 << bit_width) - 1) << (8 - bit_width)
        byte = self.read_byte(location)
        return (byte & mask) >> (8 - bit_width)

    def read_high_signed_bits(self, location, bit_width):
        assert bit_width > 0
        assert bit_width < 8
        mask = ((1 << bit_width) - 1) << (8 - bit_width)
        byte = self.read_byte(location)
        return _signed((byte & mask) >> (8 - bit_width), bit_width)

    def write_high_bits(self, location, bit_width, high_bits):
        assert bit_width > 0
        assert bit_width < 8
        high_bits = _unsigned(high_bits, bit_width) << (8 - bit_width)
        low_bits = self.read_low_bits(location, 8 - bit_width)
        self.write_byte(location, high_bits | low_bits)

    def read_bit(self, location, bit_index):
        assert bit_index >= 0
        assert bit_index < 8
        mask = 1 << (bit_index - 1)
        byte = self.read_byte(location)
        return (byte & mask) and True or False

    def write_bit(self, location, bit_index, value):
        assert bit_index >= 0
        assert bit_index < 8
        mask = 1 << (bit_index - 1)
        byte = self.read_byte(location)
        if value:
            byte |= mask
        else:
            byte &= ~mask
        self.write_byte(location, byte)

    def read_short(self, location):
        return struct.unpack_from('<H', self.data, location)[0]

    def write_short(self, location, short):
        struct.pack_into('<H', self.data, location, short)

    def read_bytes(self, location, size):
        return struct.unpack_from('%ds' % (size), self.data, location)[0]

    def read_string(self, location, size):
        return self.read_bytes(location, size).decode('ascii')

    def read_dte_battle_string(self, location, size):
        dte_battle_indices = self.read_bytes(location, size)
        return ''.join([
            DTE_BATTLE[index] or '' for index in dte_battle_indices
        ])

    def write_dte_battle_string(self, location, size, string):
        dbstr = bytes([FROM_DTE_BATTLE[c] for c in string])
        dbstr = dbstr + (b'\xff' * (size - len(dbstr)))
        struct.pack_into('%ds' % (size), self.data, location, dbstr)
