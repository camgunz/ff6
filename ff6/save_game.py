import struct

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

class SaveGame(BinaryObject):

    MaxSize = 0xA00

    CharacterOffset = 0x0
    PartyInfoOffset = 0x250
    GoldOffset = 0x260
    GameTimeOffset = 0x263
    StepsOffset = 0x266
    InventoryItemIDOffset = 0x269
    InventoryItemCountOffset = 0x369
    EsperOffset = 0x469
    ActiveGroup = 0x46D # ???
    MagicOffset = 0x46E
    BushidoOffset = 0x6F7
    BushidoNameOffset = 0x6F8
    BlitzOffset = 0x728
    LoreOffset = 0x729
    RageOffset = 0x72C
    DanceOffset = 0x74C
    SaveCountOffset = 0x7C7
    AirshipSettingsOffset = 0x8B7
    ShopActiveMembersOffset = 0x8DC
    AirshipActiveMembersOffset = 0x8DE
    MapLocationOffset = 0x960
    AirshipLocationOffset = 0x962
    WorldInfoOffset = 0x964
    PartyOffset = 0xA56

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
        self.items = []
        self.gold = 0
        self.game_time = 0
        self.steps = 0
        self.characters = []

    def serialize(self):
        pass

    def deserialize(self):
        self.items = self._load_items()
        self.gold = self.read_24(self.GoldOffset)
        self.game_time = self.read_timestamp(self.GameTimeOffset)
        self.steps = self.read_24(self.StepsOffset)
        self.characters = CharacterStructArray.deserialize(
            self,
            self.CharacterOffset
        )

    @property
    def data_offset(self):
        return self.slot * self.MaxSize

    @classmethod
    def from_file(cls, slot, rom, file_name):
        with open(file_name, 'rb') as fobj:
            return cls(slot, rom, fobj.read())

    def _load_items(self):
        fmt = '%dB' % (self.InventoryItemCount)
        ids = struct.unpack_from(fmt, self.data, self.InventoryItemIDOffset)
        counts = struct.unpack_from(
            fmt,
            self.data,
            self.InventoryItemCountOffset
        )
        return list(zip([self._rom.inventory_items[id] for id in ids], counts))
