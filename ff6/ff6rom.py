from ff6.rom import ROM
from ff6.items import Items
from ff6.monsters import Monsters

class FF6ROM(ROM):

    def __init__(self, data):
        super().__init__(data)
        self.items = Items(self)
        self.monsters = Monsters(self)

    def load(self):
        self.items.load()
        self.monsters.load()

    def save(self):
        self.items.save()
        self.monsters.save()
