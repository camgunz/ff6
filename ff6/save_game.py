from ff6 import counts, offsets

from ff6.dte import DTE_BATTLE, TO_DTE_BATTLE
from ff6.data import *
from ff6.model import BinaryModelObject
from ff6.struct import *

###
# ---------------------------------------------
# | ? | in party | front | pos | ? | team num |
# ---------------------------------------------
# | * |    *     |   *   | **  | * |    **    |
# ---------------------------------------------
###

class SaveGame(BinaryModelObject):

    Fields = (
        ArrayField(
            name='inventory_item_slots',
            offset=offsets.SaveGameInventoryItemIDs,
            count=counts.Items,
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
            count=counts.Items,
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
            count=counts.Characters,
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
                        padding_byte=b'\xff',
                        translation=(TO_DTE_BATTLE, DTE_BATTLE),
                        offset=2
                    ),
                    U8Field('level', 8),
                    U16Field('current_hp', 9),
                    U16Field('max_hp', 11),
                    U16Field('current_mp', 13),
                    U16Field('max_mp', 15),
                    U24Field('experience', 17),
                    FlagsField('status', SaveCharacterStatus, 20),
                    EnumField('battle_command1', BattleCommand, 22),
                    EnumField('battle_command2', BattleCommand, 23),
                    EnumField('battle_command3', BattleCommand, 24),
                    EnumField('battle_command4', BattleCommand, 25),
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

    Overrides = []

    MaxSize = 0xA00
    # MagicCount = 54
    # BushidoCount = 8
    # BushidoNameSize = 6
    # CharacterInfoSize = 37
    # CharacterCount = 16
    # MainCharacterCount = 12
    # InventoryItemCount = 256

    def __init__(self, data, rom, slot):
        self.slot = slot
        self.offset = self.slot * self.MaxSize
        super().__init__(data)
        self._rom = rom

    def _update_checksum(self):
        checksum = 0
        for b in self.data[:self.MaxSize-2]:
            checksum += b
            checksum &= 0xFFFF
        self.data[self.MaxSize-1] = (checksum >> 8) & 0xFF
        self.data[self.MaxSize-2] = checksum & 0xFF

    def serialize(self):
        super().serialize()
        self._update_checksum()

    @classmethod
    def from_file(cls, file_name, rom, slot):
        with open(file_name, 'rb') as fobj:
            return cls(fobj.read(), rom, slot)
