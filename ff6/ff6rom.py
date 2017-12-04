from ff6.rom import ROM
from ff6.items import Items
from ff6.monsters import Monsters

class FF6ROM(ROM):

    ItemNamesOffset             = 0x0012B500
    ItemDataOffset              = 0x00185200
    MonsterNamesOffset          = 0x000FC250
    MonsterDataOffset           = 0x000F0200
    MonsterDropsAndStealsOffset = 0x000F3200

    def __init__(self, data):
        super().__init__(data)
        self.items = Items.from_rom(self)
        self.monsters = Monsters.from_rom(self)

    @classmethod
    def from_file(cls, file_name):
        with open(file_name, 'rb') as fobj:
            return cls(fobj.read())
