from ff6 import offsets, sizes

from ff6.dte import DTE_BATTLE, TO_DTE_BATTLE
from ff6.data import *
from ff6.struct import *

"""
---------------------------------------------
| ? | in party | front | pos | ? | team num |
---------------------------------------------
| * |    *     |   *   | **  | * |    **    |
---------------------------------------------
"""

class SaveGame(BinaryModelObject):

    Fields = (
        ArrayField(
            name='inventory_item_slots',
            offset=offsets.SaveGameInventoryItemIDs,
            count=256,
            element_size=1,
            element_field=StructField(
                name='inventory_item_slot',
                offset=0,
                fields=(
                    U8Field('id', 0),
                )
            )
        ),
        ArrayField(
            name='inventory_item_slots',
            offset=offsets.SaveGameInventoryItemCounts,
            count=256,
            element_size=1,
            element_field=StructField(
                name='inventory_item_slot',
                offset=0,
                fields=(
                    U8Field('count', 0),
                )
            )
        ),
        U24Field('gold', offsets.SaveGameGold),
        TimestampField('game_time', offsets.SaveGameTime),
        U24Field('steps', offsets.SaveGameSteps),
        ArrayField(
            name='characters',
            offset=offsets.SaveGameCharacters,
            count=16,
            element_size=37,
            element_field=StructField(
                name='character',
                offset=0,
                fields=(
                    EnumField('actor', Actor, 0),
                    EnumField('character', Character, 1),
                    StrField(
                        name='name',
                        size=6,
                        translation=(DTE_BATTLE, TO_DTE_BATTLE),
                        offset=2
                    ),
                    U8Field('level', 8),
                    U16Field('current_hp', 9),
                    U16Field('max_hp', 11),
                    U16Field('current_mp', 13),
                    U16Field('max_mp', 15),
                    U24Field('experience', 17),
                    FlagsField('status', SaveCharacterStatus, 20),
                    EnumField('battle_command1', BattleCommands, 22),
                    EnumField('battle_command2', BattleCommands, 23),
                    EnumField('battle_command3', BattleCommands, 24),
                    EnumField('battle_command4', BattleCommands, 25),
                    U8Field('vigor', 26),
                    U8Field('speed', 27),
                    U8Field('stamina', 28),
                    U8Field('magic_power', 29),
                    U8Field('esper', 30),
                    U8Field('sword', 31),
                    U8Field('shield', 32),
                    U8Field('helmet', 33),
                    U8Field('armor', 34),
                    U8Field('relic1', 35),
                    U8Field('relic2', 36),
                )
            )
        )
    )

    MaxSize = 0xA00
    MagicCount = 54
    BushidoCount = 8
    BushidoNameSize = 6
    CharacterInfoSize = 37
    CharacterCount = 16
    MainCharacterCount = 12
    InventoryItemCount = 256

    def __init__(self, slot, rom, data):
        super().__init__(data)
        self.slot = slot
        self._rom = rom

    @classmethod
    def from_file(cls, slot, rom, file_name):
        with open(file_name, 'rb') as fobj:
            return cls(slot, rom, fobj.read())
