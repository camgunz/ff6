import struct

from datetime import timedelta

from ff6.dte import *

class BinaryObject:

    def __init__(self, data):
        self.data = bytearray(data)

    def read_byte(self, location):
        return read_byte(self.data, location)

    def write_byte(self, location, byte):
        write_byte(self.data, location, byte)

    def read_low_bits(self, location, bit_width):
        return read_low_bits(self.data, location, bit_width)

    def read_low_signed_bits(self, location, bit_width):
        return read_low_signed_bits(self.data, location, bit_width)

    def write_low_bits(self, location, bit_width, low_bits):
        write_low_bits(self.data, location, bit_width, low_bits)

    def read_high_bits(self, location, bit_width):
        return read_high_bits(self.data, location, bit_width)

    def read_high_signed_bits(self, location, bit_width):
        return read_high_signed_bits(self.data, location, bit_width)

    def write_high_bits(self, location, bit_width, high_bits):
        write_high_bits(self.dat, location, bit_width, high_bits)

    def read_bit(self, location, bit_index):
        return read_bit(self.data, location, bit_index)

    def write_bit(self, location, bit_index, value):
        write_bit(self.data, location, bit_index, value)

    def read_short(self, location):
        return read_short(self.data, location)

    def write_short(self, location, short):
        write_short(self.data, location, short)

    def read_24(self, location):
        return read_24(self.data, location)

    def write_24(self, location, value):
        write_24(self.data, location, value)

    def read_int(self, location):
        return read_int(self.data, location)

    def write_int(self, location, num):
        write_int(self.data, location, num)

    def read_timestamp(self, location):
        return read_timestamp(self.data, location)

    def write_timestamp(self, location, timestamp):
        return write_timestamp(self.data, location, timestamp)

    def read_bytes(self, location, size):
        return read_bytes(self.data, location, size)

    def read_string(self, location, size):
        return read_string(self.data, location, size)

    def read_dte_battle_string(self, location, size):
        return read_dte_battle_string(self.data, location, size)

    def write_dte_battle_string(self, location, size, string):
        write_dte_battle_string(self.data, location, size, string)

def _signed(num, bit_width):
    mask1 = (1 << bit_width) - 1
    mask2 = 1 << (bit_width - 1)
    num = num & mask1
    return num | (-(num & mask2))

def _unsigned(num, bit_width):
    return num & ((1 << bit_width) - 1)

def read_byte(data, location):
    return struct.unpack_from('B', data, location)[0]

def write_byte(data, location, byte):
    struct.pack_into('B', data, location, byte)

def read_low_bits(data, location, bit_width):
    assert bit_width > 0
    assert bit_width < 8
    mask = (1 << bit_width) - 1
    byte = read_byte(data, location)
    return byte & mask

def read_low_signed_bits(data, location, bit_width):
    assert bit_width > 0
    assert bit_width < 8
    mask = (1 << bit_width) - 1
    byte = read_byte(data, location)
    return _signed(byte & mask, bit_width)

def write_low_bits(data, location, bit_width, low_bits):
    assert bit_width > 0
    assert bit_width < 8
    byte = read_byte(data, location)
    high_bits = read_high_bits(data, location, 8 - bit_width) << bit_width
    write_byte(data, location, high_bits | _unsigned(low_bits, bit_width))

def read_high_bits(data, location, bit_width):
    assert bit_width > 0
    assert bit_width < 8
    mask = ((1 << bit_width) - 1) << (8 - bit_width)
    byte = read_byte(data, location)
    return (byte & mask) >> (8 - bit_width)

def read_high_signed_bits(data, location, bit_width):
    assert bit_width > 0
    assert bit_width < 8
    mask = ((1 << bit_width) - 1) << (8 - bit_width)
    byte = read_byte(data, location)
    return _signed((byte & mask) >> (8 - bit_width), bit_width)

def write_high_bits(data, location, bit_width, high_bits):
    assert bit_width > 0
    assert bit_width < 8
    high_bits = _unsigned(high_bits, bit_width) << (8 - bit_width)
    low_bits = read_low_bits(data, location, 8 - bit_width)
    write_byte(data, location, high_bits | low_bits)

def read_bit(data, location, bit_index):
    assert bit_index >= 0
    assert bit_index < 8
    mask = 1 << (bit_index - 1)
    byte = read_byte(data, location)
    return (byte & mask) and True or False

def write_bit(data, location, bit_index, value):
    assert bit_index >= 0
    assert bit_index < 8
    mask = 1 << (bit_index - 1)
    byte = read_byte(data, location)
    if value:
        byte |= mask
    else:
        byte &= ~mask
    write_byte(data, location, byte)

def read_short(data, location):
    return struct.unpack_from('<H', data, location)[0]

def write_short(data, location, short):
    struct.pack_into('<H', data, location, short)

def read_24(data, location):
    high, mid, low = struct.unpack_from('3B', data, location)
    return (low << 16) | (mid << 8) | high

def write_24(data, location, num):
    high = num >> 16
    mid = num >> 8
    low = num & 0xFF
    struct.pack_into('3B', data, location, (low, mid, high))

def read_int(data, location):
    return struct.unpack_from('<I', data, location)[0]

def write_int(data, location, num):
    struct.pack_into('<I', data, location, num)

def read_timestamp(data, location):
    high, mid, low = struct.unpack_from('3B', data, location)
    return timedelta(hours=high, minutes=mid, seconds=low)

def write_timestamp(data, location, timestamp):
    high = timestamp.seconds % 3600
    mid = timestamp.seconds % 60
    low = timestamp.seconds
    struct.pack_into('3B', data, location, (high, mid, low))

def read_bytes(data, location, size):
    return struct.unpack_from('%ds' % (size), data, location)[0]

def read_string(data, location, size):
    return read_bytes(data, location, size).decode('ascii')

def read_dte_battle_string(data, location, size):
    dte_battle_indices = read_bytes(data, location, size)
    return ''.join([
        DTE_BATTLE[index] or '' for index in dte_battle_indices
    ])

def write_dte_battle_string(data, location, size, string):
    dbstr = bytes([FROM_DTE_BATTLE[c] for c in string])
    dbstr = dbstr + (b'\xff' * (size - len(dbstr)))
    struct.pack_into('%ds' % (size), data, location, dbstr)
