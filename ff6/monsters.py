from ff6.data import *
from ff6.struct import *

_BLANKS = (366, 367, 368, 370, 371, 372, 375, 376, 378, 379, 380)

class MonsterNameStruct(Struct):

    Name   = 'MonsterNameStruct'
    Size   = 10
    Fields = (
        BattleStrField('name', Size, 0),
    )

class MonsterDataStruct(Struct):

    Name = 'MonsterDataStruct'
    Size = 32
    Fields = (
        U8Field('speed', 0),
        U8Field('strength', 1),
        U8Field('hit_rate', 2),
        U8Field('evade', 3),
        U8Field('magic_block', 4),
        U8Field('defense', 5),
        U8Field('magic_defense', 6),
        U8Field('magic_power', 7),
        U16Field('hp', 8),
        U16Field('mp', 10),
        U16Field('xp', 12),
        U16Field('gp', 14),
        U8Field('level', 16),
        Enum3HighField('morph_chance', MetamorphChance, 17),
        U5LowField('morph_package', 17),
        FlagsField('flag1', MonsterFlag1, 18),
        FlagsField('flag2', MonsterFlag2, 19),
        FlagsField('absorbed_elements', Element, 23),
        FlagsField('nullified_elements', Element, 24),
        FlagsField('weak_elements', Element, 25),
        EnumField('attack_type', MonsterAttackType, 26),
        FlagsField('immune_conditions', MonsterConditionImmunity, 27),
        FlagsField('flag3', MonsterFlag3, 30),
        Enum6LowField('special_attack_effect', MonsterSpecialAttackEffect, 31),
        BitField('special_attack_causes_no_damage', 7, 31),
    )

class MonsterNameStructArray(StructArray):

    Name = 'MonsterNameStructArray'
    Count = 381
    Struct = MonsterNameStruct

class MonsterDataStructArray(StructArray):

    Name = 'MonsterDataStructArray'
    Count = 381
    Struct = MonsterDataStruct
