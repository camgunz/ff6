from ff6 import counts, offsets, sizes

from ff6.dte import DTE_BATTLE, TO_DTE_BATTLE
from ff6.data import *
from ff6.struct import *

Espers = (
    # ArrayField(
    #     name='espers',
    #     count=counts.Espers,
    #     element_size=sizes.EsperDescription,
    #     offset=offsets.EsperDescriptions,
    #     element_field=StructField(
    #         name='esper',
    #         offset=0,
    #         fields=(
    #             StrField(
    #                 name='description',
    #                 size=sizes.EsperDescription,
    #                 translation=(TO_DTE_BATTLE, DTE_BATTLE),
    #                 offset=0
    #             ),
    #         )
    #     )
    # ),
    ArrayField(
        name='espers',
        count=counts.Espers,
        element_size=sizes.EsperAttackName,
        offset=offsets.EsperAttackNames,
        element_field=StructField(
            name='esper',
            offset=0,
            fields=(
                StrField(
                    name='attack_name',
                    size=sizes.EsperAttackName,
                    translation=(TO_DTE_BATTLE, DTE_BATTLE),
                    offset=0
                ),
            )
        )
    ),
    ArrayField(
        name='espers',
        count=counts.Espers,
        element_size=sizes.EsperName,
        offset=offsets.EsperNames,
        element_field=StructField(
            name='esper',
            offset=0,
            fields=(
                StrField(
                    name='name',
                    size=sizes.EsperName,
                    translation=(TO_DTE_BATTLE, DTE_BATTLE),
                    offset=0
                ),
            )
        )
    ),
    ArrayField(
        name='espers',
        count=counts.Espers,
        element_size=sizes.EsperData,
        offset=offsets.EsperData,
        element_field=StructField(
            name='esper',
            offset=0,
            fields=(
                U8Field('spell_learn_rate1', 0),
                U8Field('spell1', 1),
                U8Field('spell_learn_rate2', 2),
                U8Field('spell2', 3),
                U8Field('spell_learn_rate3', 4),
                U8Field('spell3', 5),
                U8Field('spell_learn_rate4', 6),
                U8Field('spell4', 7),
                U8Field('spell_learn_rate5', 8),
                U8Field('spell5', 9),
                EnumField('level_bonus', EsperBonus, 10),
            )
        )
    ),
)
