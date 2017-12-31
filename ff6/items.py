from ff6 import counts, offsets, sizes

from ff6.dte import DTE_BATTLE, TO_DTE_BATTLE
from ff6.data import *
from ff6.struct import *

InventoryItemFields = (
    Flags4HighField('usability', InventoryItemUsability, 0),
    FlagsField('targeting', Targeting, 14),
    U16Field('price', 28),
)

ItemFields = InventoryItemFields + (
    Enum3LowField('type', InventoryItemType, 0),
    FlagsField('properties', ItemProperty, 19),
    U8Field('effect_strength', 20),
    FlagsField('caused_conditions', Condition, 21),
    EnumField('special_action', ItemSpecialAction, 27),
)

UsableNonItemFields = InventoryItemFields + (
    U8Field('attack_when_used', 18),
)

ToolFields = UsableNonItemFields + (
    U8Field('attack_strength', 20),
    U8Field('hit_rate', 21),
)

EquipmentItemFields = UsableNonItemFields + (
    FlagsField('equippable_by', EquipInfo, 1),
    U8Field('spell_learn_rate', 3),
    U8Field('spell_learned', 4),
    FlagsField('field_effect', FieldEffect, 5),
    FlagsField('protected_conditions1', Condition1, 6),
    FlagsField('protected_conditions2', Condition2, 7),
    FlagsField('caused_conditions', Condition3, 8),
    FlagsField('status_effects1', StatusEffect1, 9),
    FlagsField('battle_effects1', BattleEffect1, 10),
    FlagsField('status_effects2', StatusEffect2, 11),
    FlagsField('battle_effects2', BattleEffect2, 12),
    FlagsField('battle_effects3', BattleEffect3, 13),
    FlagsField('element', Element, 15),
    S4HighField('vigor', 16),
    S4LowField('speed', 16),
    S4HighField('stamina', 17),
    S4LowField('magic_power', 17),
    U4LowField(
        name='evade',
        offset=26,
        transform_out=lambda x: x // 10,
        transform_in=lambda x: x * 10
    ),
    Enum4LowField('evade_animation', EvadeAnimation, 27),
)

WeaponFields = EquipmentItemFields + (
    FlagsField('properties', WeaponProperty, 19),
    U8Field('battle_power', 20),
    U8Field('hit_rate', 21),
    Enum4HighField('special_attack', WeaponSpecialAttack, 27),
)

DefensiveEquipmentFields = EquipmentItemFields + (
    U8Field('physical_defense', 20),
    U8Field('magic_defense', 21),
    FlagsField('absorbed_elements', Element, 22),
    FlagsField('nullified_elements', Element, 23),
    FlagsField('weak_elements', Element, 24),
    FlagsField('caused_conditions2', Condition2, 25),
    U4HighField('magic_block', 26),
)

InventoryItems = (
    ArrayField(
        name='inventory_items',
        count=counts.Items,
        element_size=sizes.InventoryItemName + 1,
        offset=offsets.InventoryItemNames,
        element_field=StructField(
            name='inventory_item',
            offset=0,
            fields=(
                EnumField('icon_type', EquipmentIconType, 0),
                StrField(
                    name='name',
                    size=sizes.InventoryItemName,
                    padding_byte=b'\xff',
                    offset=1,
                    translation=(TO_DTE_BATTLE, DTE_BATTLE)
                ),
            )
        )
    ),
    ArrayField(
        name='inventory_items',
        count=counts.Items,
        element_size=sizes.InventoryItemData,
        offset=offsets.InventoryItemData,
        element_field=VariantField(
            name='inventory_item',
            offset=0,
            field=Enum4LowField('type', InventoryItemType, 0),
            variants={
                InventoryItemType.Item: StructField(
                    name='item',
                    offset=0,
                    fields=ItemFields
                ),
                InventoryItemType.Tool: StructField(
                    name='tool',
                    offset=0,
                    fields=ToolFields
                ),
                InventoryItemType.Weapon: StructField(
                    name='weapon',
                    offset=0,
                    fields=WeaponFields
                ),
                InventoryItemType.Armor: StructField(
                    name='armor',
                    offset=0,
                    fields=DefensiveEquipmentFields
                ),
                InventoryItemType.Shield: StructField(
                    name='shield',
                    offset=0,
                    fields=DefensiveEquipmentFields
                ),
                InventoryItemType.Hat: StructField(
                    name='hat',
                    offset=0,
                    fields=DefensiveEquipmentFields
                ),
                InventoryItemType.Relic: StructField(
                    name='relic',
                    offset=0,
                    fields=DefensiveEquipmentFields
                ),
            }
        )
    )
)
