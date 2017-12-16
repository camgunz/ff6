from ff6 import offsets

from ff6.data import *
from ff6.struct import *
from ff6.bin_util import *

"""
---------------------------------------------
| ? | in party | front | pos | ? | team num |
---------------------------------------------
| * |    *     |   *   | **  | * |    **    |
---------------------------------------------
"""

class CharacterStruct(Struct):

    Name   = 'CharacterStruct'
    Size   = 37
    Fields = (
        EnumField('actor', Actor, 0),
        EnumField('character', Character, 1),
        BattleStrField('name', 6, 2),
        U8Field('level', 8),
        U16Field('current_hp', 9),
        U16Field('max_hp', 11),
        U16Field('current_mp', 13),
        U16Field('max_mp', 15),
        U24Field('experience', 17),
        FlagsField('status', SaveCharacterStatus, 20),
        FlagsField('battle_commands', BattleCommands, 22),
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

class CharacterStructArray(StructArray):

    Name   = 'CharacterStructArray'
    Count  = 16
    Struct = CharacterStruct

class InventoryItemIDStruct(Struct):

    Name = 'InventoryItemIDStruct'
    Size = 1
    Fields = (
        U8Field('id', 0),
    )

class InventoryItemCountStruct(Struct):

    name = 'InventoryItemCountStruct'
    Size = 1
    Fields = (
        U8Field('count', 0),
    )

class InventoryItemIDStructArray(StructArray):

    Name = 'InventoryItemIDStructArray'
    Count = 256
    Struct = InventoryItemIDStruct

class InventoryItemCountStructArray(StructArray):

    Name = 'InventoryItemCountStructArray'
    Count = 256
    Struct = InventoryItemCountStruct

class SaveGame(BinaryModelObject):

    Mappings = (
        BinaryMapping(
            StructArrayField(
                'inventory_item_slots',
                InventoryItemIDStructArray,
                0
            ),
            offsets.SaveGameInventoryItemIDs
        ),
        BinaryMapping(
            StructArrayField(
                'inventory_item_slots',
                InventoryItemCountStructArray,
                0
            ),
            offsets.SaveGameInventoryItemCounts
        ),
        BinaryMapping(U24Field('gold', 0), offsets.SaveGameGold),
        BinaryMapping(TimestampField('game_time', 0), offsets.SaveGameTime),
        BinaryMapping(U24Field('steps', 0), offsets.SaveGameSteps),
        BinaryMapping(
            StructArrayField('characters', CharacterStructArray, 0),
            offsets.SaveGameCharacters
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
