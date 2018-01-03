from ff6 import counts, offsets, sizes

from ff6.dte import DTE_BATTLE, TO_DTE_BATTLE
from ff6.data import *
from ff6.magic import get_magic_data_struct
from ff6.struct import *

LoreAttacks = (
    ArrayField(
        name='lore_attacks',
        count=counts.Lores,
        offset=offsets.LoreAttackData,
        element_size=sizes.MagicData,
        element_field=get_magic_data_struct('lore'),
    ),
    ArrayField(
        name='lore_attacks',
        count=counts.Lores,
        offset=offsets.LoreAttackNames,
        element_size=sizes.LoreAttackName,
        element_field=StructField(
            name='lore_attack',
            offset=0,
            fields=(
                StrField(
                    name='name',
                    size=sizes.LoreAttackName,
                    translation=(TO_DTE_BATTLE, DTE_BATTLE),
                    offset=0
                ),
            )
        )
    ),
    ArrayField(
        name='lore_attacks',
        offset=offsets.LoreAttackDescriptionPointers,
        count=counts.Lores,
        element_size=2,
        element_field=StructField(
            name='lore',
            offset=0,
            fields=(
                PointerField(
                    name='description',
                    offset=0,
                    base=offsets.LoreAttackDescriptions,
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
