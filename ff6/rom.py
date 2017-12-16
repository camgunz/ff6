from ff6.patch import Patch, PatchCommands
from ff6.struct import BinaryModelObject
from ff6.bin_util import *

class ROM(BinaryModelObject):

    def __init__(self, data):
        super().__init__(data)
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
            if command == PatchCommands.Patch:
                loc, patch_size, replacement_data = args
                self.data[loc:loc+patch_size] = replacement_data
            elif command == PatchCommands.Truncate:
                size = args[0]
                self.data = self.data[:size]
            elif command == PatchCommands.RLE:
                loc, run_size, fill_byte = args
                self.data[loc:loc+run_size] = fill_byte * run_size
            else:
                raise Exception('Unknown patch command: %s' % (command))
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
