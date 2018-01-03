from ff6 import counts, offsets, sizes

from ff6.dte import DTE_BATTLE, TO_DTE_BATTLE
from ff6.data import *
from ff6.magic import get_magic_data_struct
from ff6.struct import *

SkeanAttacks = (
    ArrayField(
        name='skean_attacks',
        count=counts.SkeanAttacks,
        offset=offsets.SkeanAttackData,
        element_size=sizes.MagicData,
        element_field=get_magic_data_struct('skean'),
    ),
    ArrayField(
        name='skean_attacks',
        count=counts.SkeanAttacks,
        offset=offsets.SkeanAttackNames,
        element_size=sizes.SkeanAttackName,
        element_field=StructField(
            name='skean_attack',
            offset=0,
            fields=(
                StrField(
                    name='name',
                    size=sizes.SkeanAttackName,
                    translation=(TO_DTE_BATTLE, DTE_BATTLE),
                    offset=0
                ),
            )
        )
    ),
)
