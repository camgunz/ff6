from ff6 import counts, offsets, sizes

from ff6.dte import DTE_BATTLE, TO_DTE_BATTLE
from ff6.data import *
from ff6.magic import get_magic_data_struct
from ff6.struct import *

Bushidos = (
    ArrayField(
        name='bushidos',
        count=counts.Bushidos,
        element_size=1,
        offset=offsets.BushidoLevels,
        element_field=StructField(
            name='bushido',
            offset=0,
            fields=(
                U8Field('level', 0),
            )
        )
    ),
    ArrayField(
        name='bushidos',
        offset=offsets.BushidoEffectData,
        count=counts.Bushidos,
        element_size=sizes.BushidoEffectData,
        element_field=get_magic_data_struct('bushido'),
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
