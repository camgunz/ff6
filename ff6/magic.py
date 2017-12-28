from ff6 import offsets, sizes

from ff6.dte import DTE_BATTLE, TO_DTE_BATTLE
from ff6.data import *
from ff6.struct import *

"""
1: Targeting - Targeting
2: Elements - Elements
3: Effect
4: Damage type (first half) Where used (second half)
5: Effect 2
6: MP Cost
7: Power
8: ?
9: ?
10: Special effect - Extra effects
11: Status 1 - Status 1
12: Status 2 - Status 2
13: Status 3 - Status 3
14: Status 4 - Status 4

- Extra effects
  - Mantra
  - Empowerer
  - Etc.

- Damage Type
  - Can use outside battle  = 1 << 0
  - Not reflectable         = 1 << 1
  - Learn if casted on      = 1 << 2
  - Enable Runic            = 1 << 3
  - Warp/Quick              = 1 << 4
  - Retarget if target dead = 1 << 5
  - Kill caster             = 1 << 6
  - Affect MP               = 1 << 7

- Status 1/2/3/4

- Elements

- Special 1
  - Physical damage
  - Spell miss if death protect
  - Etc.

- Special 2
  - Heal
  - Redirection
  - Etc.

- Special 3
  - Miss if prot. from ailments
  - Text on hit
"""

MagicStructField = StructField(
    name='magic',
    offset=0,
    fields=(
        FlagsField('targeting', Targeting, 0),
        FlagsField('elements', Element, 1),
        FlagsField('properties', MagicProperty, 2),
        U8Field('mp', 5),
        U8Field('power', 6),
        FlagsField('extra_properties', MagicPropertyExtra, 7),
        U8Field('hit_rate', 8),
        EnumField('special_effect', MagicExtraEffect, 9),
        FlagsField('caused_conditions', Condition, 10),
    )
)

Magic = (
    ArrayField(
        name='magic',
        offset=offsets.MagicData,
        count=54,
        element_size=sizes.MagicData,
        element_field=MagicStructField,
    ),
    ArrayField(
        name='magic',
        offset=offsets.MagicNames,
        count=54,
        element_size=sizes.MagicName + 1,
        element_field=StructField(
            name='magic',
            offset=0,
            fields=(
                U8Field('magic_ball', 0),
                StrField(
                    name='name',
                    size=sizes.MagicName,
                    padding_byte=b'\xff',
                    offset=1,
                    translation=(TO_DTE_BATTLE, DTE_BATTLE)
                ),
            )
        )
    ),
    ArrayField(
        name='magic',
        offset=offsets.MagicDescriptionPointers,
        count=54,
        element_size=2,
        element_field=StructField(
            name='magic',
            offset=0,
            fields=(
                PointerField(
                    name='description',
                    offset=0,
                    base=offsets.MagicDescriptions,
                    pointer_field=U16Field(name='pointer', offset=0),
                    target_field=StrField(
                        name='description',
                        terminator=b'\x00',
                        offset=0,
                        translation=(TO_DTE_BATTLE, DTE_BATTLE)
                    ),
                ),
            )
        )
    )
)
