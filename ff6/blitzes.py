from ff6 import counts, offsets, sizes

from ff6.dte import DTE_BATTLE, TO_DTE_BATTLE
from ff6.data import *
from ff6.struct import *

Blitzes = (
    ArrayField(
        name='blitzes',
        count=counts.Blitzes,
        element_size=1,
        offset=offsets.BlitzLevels,
        element_field=StructField(
            name='blitz',
            offset=0,
            fields=(
                U8Field('level', 0),
            )
        )
    ),
    ArrayField(
        name='blitzes',
        offset=offsets.BlitzEffectData,
        count=counts.Blitzes,
        element_size=sizes.BlitzEffectData,
        element_field=StructField(
            name='blitz',
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
    ),
    ArrayField(
        name='blitzes',
        count=counts.Blitzes,
        element_size=sizes.BlitzName,
        offset=offsets.BlitzNames,
        element_field=StructField(
            name='blitz',
            offset=0,
            fields=(
                StrField(
                    name='name',
                    size=sizes.BlitzName,
                    translation=(TO_DTE_BATTLE, DTE_BATTLE),
                    offset=0
                ),
            )
        )
    ),
    ArrayField(
        name='blitzes',
        offset=offsets.BlitzDescriptionPointers,
        count=counts.Blitzes,
        element_size=2,
        element_field=StructField(
            name='blitz',
            offset=0,
            fields=(
                PointerField(
                    name='description',
                    offset=0,
                    base=offsets.BlitzDescriptions,
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
    ),
)
