from ff6.hp import HPPerLevel
from ff6.mp import MPPerLevel
from ff6.xp import XPPerLevel
from ff6.rom import ROM
from ff6.items import InventoryItems
from ff6.magic import Magic
from ff6.model import *
from ff6.shops import Shops
from ff6.dances import Dances, DanceAttacks
from ff6.espers import Espers, EsperLevelBonuses
from ff6.blitzes import Blitzes
from ff6.bushido import Bushidos
from ff6.monsters import Monsters
from ff6.lore_attacks import LoreAttacks
from ff6.magitek_menu import MagitekMenu
from ff6.misc_attacks import MiscAttacks
from ff6.slot_attacks import SlotAttacks
from ff6.skean_attacks import SkeanAttacks
from ff6.magitek_attacks import MagitekAttacks
from ff6.monster_attacks import MonsterAttacks
from ff6.natural_magic import CelesNaturalMagic, TerraNaturalMagic
from ff6.morph_packages import MorphPackages
from ff6.character_starts import CharacterStarts
from ff6.desperation_attacks import DesperationAttacks
from ff6.battle_dialogue import (BattleDialogues1, BattleDialogues2,
                                 BattleMessages)
from ff6.battle_formations import BattleFormations

class FF6ROM(ROM):

    Fields = (
        InventoryItems +
        Monsters +
        Blitzes +
        Bushidos +
        Magic +
        HPPerLevel +
        MPPerLevel +
        XPPerLevel +
        MorphPackages +
        CharacterStarts +
        Espers +
        CelesNaturalMagic +
        TerraNaturalMagic +
        Shops +
        SkeanAttacks +
        Dances +
        DanceAttacks +
        SlotAttacks +
        MagitekAttacks +
        LoreAttacks +
        MonsterAttacks +
        DesperationAttacks +
        MiscAttacks +
        MagitekMenu +
        EsperLevelBonuses +
        BattleDialogues1 +
        BattleDialogues2 +
        BattleMessages +
        BattleFormations
    )

    Overrides = (
        (('monsters', Item, 'steal1'), Index(('inventory_items',))),
        (('monsters', Item, 'steal2'), Index(('inventory_items',))),
        (('monsters', Item, 'drop1'), Index(('inventory_items',))),
        (('monsters', Item, 'drop2'), Index(('inventory_items',))),
        (
            ('inventory_items', Item, 'spell_learned'),
            Index(('magic',))
        ),
        (('inventory_items', Item, 'colosseum_monster'), Index(('monsters',))),
        (
            ('inventory_items', Item, 'colosseum_prize'),
            Index(('inventory_items',))
        ),
        (('character_starts', Item, 'weapon'), Index(('inventory_items',))),
        (('character_starts', Item, 'weapon'), Index(('inventory_items',))),
        (('character_starts', Item, 'shield'), Index(('inventory_items',))),
        (('character_starts', Item, 'hat'), Index(('inventory_items',))),
        (('character_starts', Item, 'armor'), Index(('inventory_items',))),
        (('character_starts', Item, 'relic1'), Index(('inventory_items',))),
        (('character_starts', Item, 'relic2'), Index(('inventory_items',))),
        (('espers', Item, 'spell1'), Index(('magic',), {255: None})),
        (('espers', Item, 'spell2'), Index(('magic',), {255: None})),
        (('espers', Item, 'spell3'), Index(('magic',), {255: None})),
        (('espers', Item, 'spell4'), Index(('magic',), {255: None})),
        (('espers', Item, 'spell5'), Index(('magic',), {255: None})),
        (
            ('espers', Item, 'level_bonus'),
            Index(('esper_level_bonuses',), {255: None})
        ),
        (('celes_natural_magic', Item, 'spell'), Index(('magic',))),
        (('terra_natural_magic', Item, 'spell'), Index(('magic',))),
        (('shops', Item, 'item1'), Index(('inventory_items',))),
        (('shops', Item, 'item2'), Index(('inventory_items',))),
        (('shops', Item, 'item3'), Index(('inventory_items',))),
        (('shops', Item, 'item4'), Index(('inventory_items',))),
        (('shops', Item, 'item5'), Index(('inventory_items',))),
        (('shops', Item, 'item6'), Index(('inventory_items',))),
        (('shops', Item, 'item7'), Index(('inventory_items',))),
        (('shops', Item, 'item8'), Index(('inventory_items',))),
        (
            ('magitek_menu', Item, 'commands'),
            SplitIndex(
                (
                    (range(  0,   8), ('magitek_attacks',)),
                    (range(  8,  32), ('lore_attacks',)),
                    (range( 32, 109), ('monster_attacks',)),
                    (range(109, 117), ('desperation_attacks',)),
                    (range(109, 117), ('misc_attacks',)),
                ),
                {255: None}
            )
        ),
        (
            ('magitek_menu', Item, 'terra_commands'),
            SplitIndex(
                (
                    (range(  0,   8), ('magitek_attacks',)),
                    (range(  8,  32), ('lore_attacks',)),
                    (range( 32, 109), ('monster_attacks',)),
                    (range(109, 117), ('desperation_attacks',)),
                    (range(109, 117), ('misc_attacks',)),
                ),
                {255: None}
            )
        ),
        (('battle_formations', Item, 'enemy1'), Index(('monsters',), {255: None})),
        (('battle_formations', Item, 'enemy2'), Index(('monsters',), {255: None})),
        (('battle_formations', Item, 'enemy3'), Index(('monsters',), {255: None})),
        (('battle_formations', Item, 'enemy4'), Index(('monsters',), {255: None})),
        (('battle_formations', Item, 'enemy5'), Index(('monsters',), {255: None})),
        (('battle_formations', Item, 'enemy6'), Index(('monsters',), {255: None})),
    )
