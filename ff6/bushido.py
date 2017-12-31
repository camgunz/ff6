from ff6 import counts, offsets, sizes

from ff6.dte import DTE_BATTLE, TO_DTE_BATTLE
from ff6.data import *
from ff6.struct import *

Bushidos = (
    ArrayField(
        name='bushidos',
        offset=offsets.BushidoEffectData,
        count=counts.Bushidos,
        element_size=sizes.BushidoEffectData,
        element_field=StructField(
            name='bushido',
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
        name='bushidos',
        count=counts.Bushidos,
        element_size=sizes.BushidoName,
        offset=offsets.BushidoNames,
        element_field=StructField(
            name='bushido',
            offset=0,
            fields=(
                StrField(
                    name='name',
                    size=sizes.BushidoName,
                    translation=(TO_DTE_BATTLE, DTE_BATTLE),
                    offset=0
                ),
            )
        )
    ),
    ArrayField(
        name='bushidos',
        offset=offsets.BushidoDescriptionPointers,
        count=counts.Bushidos,
        element_size=2,
        element_field=StructField(
            name='bushido',
            offset=0,
            fields=(
                PointerField(
                    name='description',
                    offset=0,
                    base=offsets.BushidoDescriptions,
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
