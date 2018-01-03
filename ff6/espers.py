from ff6 import counts, offsets, sizes

from ff6.dte import DTE_BATTLE, TO_DTE_BATTLE
from ff6.data import *
from ff6.magic import get_magic_data_struct
from ff6.struct import *

EsperLevelBonuses = (
    ArrayField(
        name='esper_level_bonuses',
        count=counts.EsperLevelBonuses,
        offset=offsets.ShortEsperLevelBonusDescriptions,
        element_size=sizes.ShortEsperLevelBonusDescription,
        element_field=StructField(
            name='esper_level_bonus',
            offset=0,
            fields=(
                StrField(
                    name='short_description',
                    offset=0,
                    size=sizes.ShortEsperLevelBonusDescription,
                    translation=(TO_DTE_BATTLE, DTE_BATTLE),
                ),
            )
        )
    ),
    ArrayField(
        name='esper_level_bonuses',
        count=counts.EsperLevelBonuses,
        offset=offsets.EsperLevelBonusDescriptionPointers,
        element_size=2,
        element_field=StructField(
            name='esper_level_bonus',
            offset=0,
            fields=(
                PointerField(
                    name='description',
                    offset=0,
                    base=offsets.EsperLevelBonusDescriptions,
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
        element_size = sizes.MagicData,
        offset=offsets.EsperAttackData,
        element_field=get_magic_data_struct('esper'),
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
