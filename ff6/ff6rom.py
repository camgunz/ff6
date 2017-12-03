from ff6.rom import ROM
from ff6.items import Items

class FF6ROM(ROM):

    ItemNamesOffset = 0x12B500
    ItemDataOffset = 0x185200

    def __init__(self, data):
        super().__init__(data)
        self.items = Items.from_rom(self)

    @classmethod
    def from_file(cls, file_name):
        with open(file_name, 'rb') as fobj:
            return cls(fobj.read())
