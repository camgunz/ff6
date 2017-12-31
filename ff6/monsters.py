from ff6 import counts, offsets, sizes

from ff6.dte import DTE_BATTLE, TO_DTE_BATTLE
from ff6.data import *
from ff6.struct import *

_BLANKS = (366, 367, 368, 370, 371, 372, 375, 376, 378, 379, 380)

Monsters = (
    ArrayField(
        name='monsters',
        offset=offsets.MonsterNames,
        count=counts.Monsters,
        element_size=sizes.MonsterName,
        element_field=StructField(
            name='monster',
            offset=0,
            fields=(
                StrField(
                    name='name',
                    size=sizes.MonsterName,
                    offset=0,
                    translation=(TO_DTE_BATTLE, DTE_BATTLE)
                ),
            )
        )
    ),
    ArrayField(
        name='monsters',
        offset=offsets.MonsterData,
        count=counts.Monsters,
        element_size=32,
        element_field=StructField(
            name='monster',
            offset=0,
            fields=(
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
                Enum6LowField('special_attack_effect',
                              MonsterSpecialAttackEffect, 31),
                BitField('special_attack_causes_no_damage', 7, 31),
            )
        )
    ),
    ArrayField(
        name='monsters',
        offset=offsets.MonsterDropsAndSteals,
        count=counts.Monsters,
        element_size=4,
        element_field=StructField(
            name='monster',
            offset=0,
            fields=(
                U8Field('drop1', 0),
                U8Field('drop2', 1),
                U8Field('steal1', 2),
                U8Field('steal2', 3),
            )
        )
    ),
    ArrayField(
        name='monsters',
        offset=offsets.SketchData,
        count=counts.Monsters,
        element_size=2,
        element_field=StructField(
            name='monster',
            offset=0,
            fields=(
                U8Field('sketch1', 0),
                U8Field('sketch2', 1),
            )
        )
    ),
    ArrayField(
        name='monsters',
        offset=offsets.ControlData,
        count=counts.Monsters,
        element_size=4,
        element_field=StructField(
            name='monster',
            offset=0,
            fields=(
                U8Field('control1', 0),
                U8Field('control2', 1),
                U8Field('control3', 2),
                U8Field('control4', 3),
            )
        )
    ),
    ArrayField(
        name='monsters',
        offset=offsets.RageData,
        count=counts.Monsters,
        element_size=2,
        element_field=StructField(
            name='monster',
            offset=0,
            fields=(
                U8Field('rage1', 0),
                U8Field('rage2', 1),
            )
        )
    )
)
