import os
import struct

import lib

class Patch:

    HEADER_BYTES = tuple([ord(c) for c in 'PATCH'])
    EOF_BYTES = tuple([ord(c) for c in 'EOF'])

    def __init__(self, file_name, header, apply, notes, data):
        if struct.unpack_from('5B', data) != self.HEADER_BYTES:
            raise Exception('Invalid IPS patch data')
        self.file_name = file_name
        self.header = header
        self.apply = apply
        self.notes = notes
        self.data = bytearray(data)

    @staticmethod
    def from_file(file_path, header, apply, notes):
        file_name = os.path.basename(file_path)
        with open(file_path, 'rb') as fobj:
            return Patch(file_name, header, apply, notes, fobj.read())

    @staticmethod
    def from_roms(file_name, header, apply, notes, base_rom, modded_rom):
        ###
        # For simplicity, don't make any RLEs.
        ###
        diffs = []
        in_diff = False
        location = None
        size = None
        for n in range(len(base_rom.data)):
            base_rom_byte = base_rom.data[n]
            modded_rom_byte = modded_rom.data[n]
            if in_diff:
                if base_rom_byte != modded_rom_byte:
                    size += 1
                else:
                    diffs.append((location, size))
                    in_diff = False
                    location = None
                    size = None
            elif base_rom_byte != modded_rom_byte:
                in_diff = True
                location = n
                size = 1
        data = bytearray()
        data.extend(struct.pack('5B', *[int(b) for b in Patch.HEADER_BYTES]))
        for location, size in diffs:
            location_bytes = (
                (location & 0x00FF0000) >> 16,
                (location & 0x0000FF00) >> 8,
                (location & 0x000000FF)
            )
            size_bytes = (
                (size & 0x0000FF00) >> 8,
                (size & 0x000000FF)
            )
            data_bytes = modded_rom.data[location:location+size]
            data.extend(struct.pack('3B', *location_bytes))
            data.extend(struct.pack('2B', *size_bytes))
            data.extend(struct.pack('{}s'.format(size), data_bytes))
        data.extend(struct.pack('3B', *[int(b) for b in Patch.EOF_BYTES]))
        return Patch(file_name, header, apply, notes, data)

    def __eq__(self, other):
        return self.file_name == other.file_name

    def __iter__(self):
        offset = 0
        header = struct.unpack_from('5B', self.data)
        offset += 5
        if header != Patch.HEADER_BYTES:
            raise Exception('Invalid IPS patch data')
        while offset < len(self.data):
            start_offset = offset
            loc = struct.unpack_from('3B', self.data, offset=offset)
            offset += 3
            if loc == Patch.EOF_BYTES:
                if len(self.data) - offset == 3:
                    truncate = struct.unpack_from(
                        '3B',
                        self.data,
                        offset=offset
                    )
                    offset += 3
                    truncate = (
                        (truncate[0] << 16) +
                        (truncate[1] << 8) +
                        (truncate)
                    )
                    yield ('truncate', (truncate,))
                    self.data = self.data[:truncate]
                break
            loc = ((loc[0] << 16) + (loc[1] << 8)  + (loc[2]))
            patch_size = struct.unpack_from('!H', self.data, offset=offset)
            offset += 2
            patch_size = patch_size[0]
            if patch_size == 0:
                run_size = struct.unpack_from('!H', self.data, offset=offset)
                offset += 2
                run_size = run_size[0]
                fill_byte = struct.unpack_from('c', self.data, offset=offset)
                offset += 1
                fill_byte = fill_byte[0]
                yield ('rle', (loc, run_size, fill_byte))
            else:
                replacement_data = struct.unpack_from(
                    '{}s'.format(patch_size),
                    self.data,
                    offset
                )
                offset += patch_size
                replacement_data = replacement_data[0]
                yield ('patch', (loc, patch_size, replacement_data))

    def save(self):
        config = lib.get_config()
        patch_file_path = os.path.join(config['patch_dir'], self.file_name)
        with open(patch_file_path, 'wb') as patch_fobj:
            patch_fobj.write(self.data)
        patch_list = lib.get_patch_list()
        if self not in patch_list:
            patch_list.append(self)
        lib.save_patch_list()

# vi: et sw=4 ts=4 tw=79
