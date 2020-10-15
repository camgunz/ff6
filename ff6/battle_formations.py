from ff6 import counts, offsets, sizes

from ff6.data import *
from ff6.struct import *

PositionFields = (
    U4HighField('x', 0),
    U4LowField('y', 0),
)

BattleFormations = (
    ArrayField(
        name='battle_formations',
        count=counts.BattleFormations,
        element_size=sizes.BattleFormationEnemyData,
        offset=offsets.BattleFormationEnemyData,
        element_field=StructField(
            name='battle_formation',
            offset=0,
            fields=(
                FlagsField(
                    name='present_enemies',
                    offset=1,
                    enum=BattleFormationPresentEnemies,
                ),
                U8Field('enemy1', 2),
                U8Field('enemy2', 3),
                U8Field('enemy3', 4),
                U8Field('enemy4', 5),
                U8Field('enemy5', 6),
                U8Field('enemy6', 7),
                StructField(
                    name='enemy1_position',
                    offset=8,
                    fields=PositionFields
                ),
                StructField(
                    name='enemy2_position',
                    offset=9,
                    fields=PositionFields
                ),
                StructField(
                    name='enemy3_position',
                    offset=10,
                    fields=PositionFields
                ),
                StructField(
                    name='enemy4_position',
                    offset=11,
                    fields=PositionFields
                ),
                StructField(
                    name='enemy5_position',
                    offset=12,
                    fields=PositionFields
                ),
                StructField(
                    name='enemy6_position',
                    offset=13,
                    fields=PositionFields
                ),
                FlagsField('boss_enemies', BattleFormationBossEnemies, 14)
            )
        )
    ),
    ArrayField(
        name='battle_formations',
        count=counts.BattleFormations,
        element_size=sizes.BattleFormationData,
        offset=offsets.BattleFormationData,
        element_field=StructField(
            name='battle_formation',
            offset=0,
            fields=(
                FlagsField('flags1', BattleFormationFlags1, 0),
                FlagsField('flags2', BattleFormationFlags2, 1),
                U8Field('battle_event_script', 2),
                FlagsField('flags3', BattleFormationFlags3, 3),
            )
        )
    )
)
