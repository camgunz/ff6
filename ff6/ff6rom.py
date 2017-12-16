from ff6 import offsets

from ff6.rom import ROM
from ff6.items import *
from ff6.monsters import *

class InventoryItems(StructArrayAggregate):

    ElementName = 'InventoryItem'
    StructArraysAndLocations = (
        (InventoryItemNameStructArray, offsets.InventoryItemNames),
        (InventoryItemDataStructArray, offsets.InventoryItemData),
    )

class Monsters(StructArrayAggregate):

    ElementName = 'Monster'
    StructArraysAndLocations = (
        (MonsterNameStructArray, offsets.MonsterNames),
        (MonsterDataStructArray, offsets.MonsterData)
    )

class FF6ROM(ROM):

    Mappings = (
        ('inventory_items', InventoryItems),
        ('monsters', Monsters)
    )

    def serialize(self):
        for name, aggregate in self.Mappings:
            aggregate.serialize(self, getattr(self, name))

    def deserialize(self):
        for name, aggregate in self.Mappings:
            setattr(self, name, aggregate.deserialize(self))
