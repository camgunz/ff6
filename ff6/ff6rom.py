from ff6.rom import ROM
from ff6.items import InventoryItems
from ff6.monsters import Monsters
from ff6.struct import BinaryModel

class FF6ROM(ROM, BinaryModel):

    Fields = InventoryItems + Monsters
