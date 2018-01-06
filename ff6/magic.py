from ff6 import counts, offsets, sizes

from ff6.dte import DTE_BATTLE, TO_DTE_BATTLE
from ff6.data import *
from ff6.struct import *

def get_magic_data_struct(name):
    return StructField(
        name=name,
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
        count=counts.Magic,
        element_size=sizes.MagicData,
        element_field=get_magic_data_struct('name'),
    ),
    ArrayField(
        name='magic',
        offset=offsets.MagicNames,
        count=counts.Magic,
        element_size=sizes.MagicName + 1,
        element_field=StructField(
            name='magic',
            offset=0,
            fields=(
                EnumField('magic_ball', MagicBall, 0),
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
        count=counts.Magic,
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
