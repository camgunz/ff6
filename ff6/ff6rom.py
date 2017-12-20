from ff6.hp import HPPerLevel
from ff6.mp import MPPerLevel
from ff6.xp import XPPerLevel
from ff6.rom import ROM
from ff6.items import InventoryItems
from ff6.struct import BinaryModel
from ff6.blitzes import BlitzNames
from ff6.bushido import BushidoNames
from ff6.monsters import Monsters
from ff6.magic import BlackMagic, GreyMagic, WhiteMagic
from ff6.morph_packages import MorphPackages
from ff6.character_starts import CharacterStarts

class FF6ROM(ROM, BinaryModel):

    Fields = (
        InventoryItems +
        Monsters +
        BlitzNames +
        BushidoNames +
        BlackMagic +
        GreyMagic +
        WhiteMagic +
        HPPerLevel +
        MPPerLevel +
        XPPerLevel +
        MorphPackages +
        CharacterStarts
    )
