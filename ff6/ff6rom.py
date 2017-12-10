from ff6.rom import ROM
from ff6.items import Items
from ff6.monsters import Monsters

class FF6ROM(ROM):

    MonsterDropsAndStealsOffset = 0x000F3200

    def __init__(self, data):
        super().__init__(data)
        self.items = Items(self)
        self.monsters = Monsters(self)

    @classmethod
    def from_file(cls, file_name):
        with open(file_name, 'rb') as fobj:
            return cls(fobj.read())
