import struct

class Patch:

    HEADER_BYTES = tuple([ord(c) for c in 'PATCH'])
    EOF_BYTES = tuple([ord(c) for c in 'EOF'])

    def __init__(self, file_name, header, apply, notes, data):
        if struct.unpack('5B', data) != self.HEADER_BYTES:
            raise Exception('Invalid IPS patch data')
        self.file_name = file_name
        self.header = header
        self.apply = apply
        self.notes = notes
        self.data = data

    @staticmethod
    def from_file(file_name, header, apply, notes):
        with open(file_name, 'rb') as fobj:
            data = bytearray(fobj.read())
            return Patch(file_name, header, apply, notes, data)

    @staticmethod
    def from_roms(base_rom, modded_rom):
        ###
        # For simplicity, don't make any RLEs.
        ###
        diffs = []
        current_diff = None # will be 2-Tuple (location, size)
        for n in range(len(base_rom.data)):
            base_rom_byte = base_rom.data[n]
            modded_rom_byte = modded_rom.data[n]
            if current_diff:
                if base_rom_byte != modded_rom_byte:
                    current_diff[1] += 1
                else:
                    diffs.append(current_diff)
                    current_diff = None
            elif base_rom_byte != modded_rom_byte:
                current_diff = (n, 1)
        data = bytearray()
        offset = 0
        struct.pack_into('5B', data, offset, *self.HEADER_BYTES)
        offset += 5
        for location, size in diffs:
            location_bytes = (
                (location & 0x00FF0000),
                (location & 0x0000FF00),
                (location & 0x000000FF)
            )
            size_bytes = (
                (size & 0x0000FF00),
                (size & 0x000000FF)
            )
            data = modded_rom.data[location:location+size]
            struct.pack_into('3B', data, offset, *location_bytes)
            offset += 3
            struct.pack_into('2B', data, offset, *size_bytes)
            offset += 2
            struct.pack_into('{}s'.format(size), data, offset, *data_bytes)
            offset += size
        struct.pack_into('3B', data, offset, *self.EOF_BYTES)

    def __eq__(self, other):
        return self.file_name == other.file_name

    def __iter__(self):
        offset = 0
        header = struct.unpack_from('5B', patch_data)
        offset += 5
        if header != Patch.HEADER_BYTES:
            raise Exception('Invalid IPS patch data')
        while offset < len(patch_data):
            start_offset = offset
            loc = struct.unpack_from('3B', patch_data, offset=offset)
            offset += 3
            if loc == Patch.EOF_BYTES:
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
                    yield ('truncate', (truncate,))
                    self.data = self.data[:truncate]
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
                yield ('rle', (loc, run_size, fill_byte))
            else:
                replacement_data = struct.unpack_from(
                    '{}s'.format(patch_size),
                    patch_data,
                    offset
                )
                offset += patch_size
                replacement_data = replacement_data[0]
                yield ('patch', (loc, patch_size, replacement_data))

    def save(self):
        patch_file_path = os.path.join(config['patch_dir'], self.file_name)
        with open(patch_file_path, 'w') as patch_fobj:
            patch_fobj.write(self.data)
        patch_list = lib.get_patch_list()
        if self not in patch_list:
            patch_list.append(self)
        lib.save_patch_list()

# vi: et sw=4 ts=4 tw=79
