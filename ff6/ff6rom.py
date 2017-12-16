from ff6 import offsets

from ff6.rom import ROM
from ff6.items import *
from ff6.struct import *
from ff6.monsters import *

class FF6ROM(ROM, BinaryModel):

    Mappings = (
        BinaryMapping(
            StructArrayField(
                'inventory_items',
                InventoryItemNameStructArray,
                0
            ),
            offsets.InventoryItemNames
        ),
        BinaryMapping(
            StructArrayField(
                'inventory_items',
                InventoryItemDataStructArray,
                0
            ),
            offsets.InventoryItemData
        ),
        BinaryMapping(
            StructArrayField('monsters', MonsterNameStructArray, 0),
            offsets.MonsterNames
        ),
        BinaryMapping(
            StructArrayField('monsters', MonsterDataStructArray, 0),
            offsets.MonsterData
        )
    )
