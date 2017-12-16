from ff6.rom import ROM
from ff6.items import (InventoryItemNameStructArray,
                       InventoryItemDataStructArray)
from ff6.monsters import MonsterNameStructArray, MonsterDataStructArray

class FF6ROM(ROM):

    InventoryItemNameOffset = 0x0012B500
    InventoryItemDataOffset = 0x00185200
    MonsterNameOffset       = 0x000FC250
    MonsterDataOffset       = 0x000F0200

    def __init__(self, data):
        super().__init__(data)
        self.inventory_item_names = []
        self.inventory_item_data = []
        self.monster_names = []
        self.monster_data = []

    def save(self):
        InventoryItemNameStructArray.serialize(
            self,
            self.InventoryItemNameOffset,
            self.inventory_item_names
        )
        InventoryItemDataStructArray.serialize(
            self,
            self.InventoryItemDataOffset,
            self.inventory_item_data
        )
        MonsterNameStructArray.serialize(
            self,
            self.MonsterNameOffset,
            self.monster_names
        )
        MonsterDataStructArray.serialize(
            self,
            self.MonsterDataOffset,
            self.monster_data
        )

    def load(self):
        self.inventory_item_names = InventoryItemNameStructArray.deserialize(
            self,
            self.InventoryItemNameOffset
        )
        self.inventory_item_data = InventoryItemDataStructArray.deserialize(
            self,
            self.InventoryItemDataOffset
        )
        self.monster_names = MonsterNameStructArray.deserialize(
            self,
            self.MonsterNameOffset
        )
        self.monster_data = MonsterDataStructArray.deserialize(
            self,
            self.MonsterDataOffset
        )
