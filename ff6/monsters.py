from ff6.data import *
# from ff6.type_checks import *
from ff6.typed_object import *

class Monster(FF6Object):

    NameSize   = 10
    NameOffset = 0x000FC250
    DataOffset = 0x000F0200
    DataSize   = 32
    TypeName   = 'Monster'

    @property
    def name_offset(self):
        return self.NameOffset + (self.NameSize * self.number)

    @property
    def data_offset(self):
        return self.DataOffset + (self.DataSize * self.number)

    def _build_fields(self):
        return super()._build_fields() + (
            BattleStrField(self, 'name', self.NameSize, self.name_offset + 0),
            U8Field(self, 'speed', self.data_offset + 0),
            U8Field(self, 'strength', self.data_offset + 1),
            U8Field(self, 'hit_rate', self.data_offset + 2),
            U8Field(self, 'evade', self.data_offset + 3),
            U8Field(self, 'magic_block', self.data_offset + 4),
            U8Field(self, 'defense', self.data_offset + 5),
            U8Field(self, 'magic_defense', self.data_offset + 6),
            U8Field(self, 'magic_power', self.data_offset + 7),
            U16Field(self, 'hp', self.data_offset + 8),
            U16Field(self, 'mp', self.data_offset + 10),
            U16Field(self, 'xp', self.data_offset + 12),
            U16Field(self, 'gp', self.data_offset + 14),
            U8Field(self, 'level', self.data_offset + 16),
            Enum3HighField(self, 'morph_chance', MetamorphChance,
                           self.data_offset + 17),
            U8Field(self, 'morph_package', self.data_offset + 17),
            Flags8Field(self, MonsterFlag1, self.data_offset + 18),
            Flags8Field(self, MonsterFlag2, self.data_offset + 19),
            Flags8Field(self, MonsterFlag3, self.data_offset + 30),
            Flags8Field(self, Element, self.data_offset + 23,
                        prefix='absorbed_'),
            Flags8Field(self, Element, self.data_offset + 24,
                        prefix='nullified_'),
            Flags8Field(self, Element, self.data_offset + 25,
                        prefix='weak_to_'),
            Enum8Field(self, 'attack_type', MonsterAttackType,
                       self.data_offset + 26),
            Flags8Field(self, Condition1, self.data_offset + 27,
                        prefix='immune_to_'),
            Flags8Field(self, Condition2, self.data_offset + 28,
                        prefix='immune_to_'),
            Flags8Field(self, Condition3, self.data_offset + 29,
                        prefix='immune_to_'),
            Enum6LowField(self, 'special_attack_effect',
                          MonsterSpecialAttackEffect, self.data_offset + 31),
            BitField(self, 'special_attack_causes_no_damage', 7,
                     self.data_offset + 31),
            U8Field(self, 'field1', self.data_offset + 1),
            U8Field(self, 'field2', self.data_offset + 2),
            U8Field(self, 'field3', self.data_offset + 3),
            U8Field(self, 'field4', self.data_offset + 4),
            U8Field(self, 'field5', self.data_offset + 5),
            U8Field(self, 'field6', self.data_offset + 6),
            U8Field(self, 'field7', self.data_offset + 7),
            U8Field(self, 'field8', self.data_offset + 8),
            U8Field(self, 'field9', self.data_offset + 9),
            U8Field(self, 'field10', self.data_offset + 10),
            U8Field(self, 'field11', self.data_offset + 11),
            U8Field(self, 'field12', self.data_offset + 12),
            U8Field(self, 'field13', self.data_offset + 13),
            U8Field(self, 'field14', self.data_offset + 14),
            U8Field(self, 'field15', self.data_offset + 15),
            U8Field(self, 'field16', self.data_offset + 16),
            U8Field(self, 'field17', self.data_offset + 17),
            U8Field(self, 'field18', self.data_offset + 18),
            U8Field(self, 'field19', self.data_offset + 19),
            U8Field(self, 'field20', self.data_offset + 20),
            U8Field(self, 'field21', self.data_offset + 21),
            U8Field(self, 'field22', self.data_offset + 22),
            U8Field(self, 'field23', self.data_offset + 23),
            U8Field(self, 'field24', self.data_offset + 24),
            U8Field(self, 'field25', self.data_offset + 25),
            U8Field(self, 'field26', self.data_offset + 26),
            U8Field(self, 'field27', self.data_offset + 27),
            U8Field(self, 'field28', self.data_offset + 28),
            U8Field(self, 'field29', self.data_offset + 29),
            U8Field(self, 'field30', self.data_offset + 30),
            U8Field(self, 'field31', self.data_offset + 31),
        )

    def save_to_rom(self):
        for field in self.fields:
            field.save_to_rom()

class Monsters(TypedObjectContainer):

    ObjectCount = 381
    Blanks = (366, 367, 368, 370, 371, 372, 375, 376, 378, 379, 380)
    ObjectType = Monster
    Name = 'Monsters'
