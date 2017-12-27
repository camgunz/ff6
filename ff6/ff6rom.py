from ff6.hp import HPPerLevel
from ff6.mp import MPPerLevel
from ff6.xp import XPPerLevel
from ff6.rom import ROM
from ff6.items import InventoryItems
from ff6.model import *
from ff6.blitzes import BlitzNames
from ff6.bushido import BushidoNames
from ff6.monsters import Monsters
# from ff6.magic import BlackMagic, GreyMagic, WhiteMagic
from ff6.magic import Magic
from ff6.morph_packages import MorphPackages
from ff6.character_starts import CharacterStarts

class FF6ROM(ROM):

    Fields = (
        InventoryItems +
        Monsters +
        BlitzNames +
        BushidoNames +
        Magic +
        # BlackMagic +
        # GreyMagic +
        # WhiteMagic +
        HPPerLevel +
        MPPerLevel +
        XPPerLevel +
        MorphPackages +
        CharacterStarts
    )

    Overrides = (
        (('monsters', Item, 'steal1'), Index(('inventory_items',))),
        (('monsters', Item, 'steal2'), Index(('inventory_items',))),
        (('monsters', Item, 'drop1'), Index(('inventory_items',))),
        (('monsters', Item, 'drop2'), Index(('inventory_items',))),
        (
            ('inventory_items', Item, 'spell_learned'),
            Index(('inventory_items',))
        ),
        (('character_starts', Item, 'weapon'), Index(('inventory_items',)))
        (('character_starts', Item, 'weapon'), Index(('inventory_items',))),
        (('character_starts', Item, 'shield'), Index(('inventory_items',))),
        (('character_starts', Item, 'hat'), Index(('inventory_items',))),
        (('character_starts', Item, 'armor'), Index(('inventory_items',))),
        (('character_starts', Item, 'relic1'), Index(('inventory_items',))),
        (('character_starts', Item, 'relic2'), Index(('inventory_items',))),
    )
