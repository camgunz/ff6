from ff6.data import *
from ff6.struct import *

NameSize   = 13
DataSize   = 30

class InventoryItemNameStruct(Struct):

    Name = 'InventoryItemNameStruct'
    Size = 13
    Fields = (
        EnumField('icon_type', EquipmentIconType, 0),
        BattleStrField('name', Size - 1, 1)
    )

class InventoryItemStruct(Struct):

    Name = 'InventoryItemStruct'
    Size = 30
    Fields = (
        Flags4HighField('usability', InventoryItemUsability, 0),
        FlagsField('targeting', Targeting, 14),
        U16Field('price', 28),
    )

class ItemStruct(InventoryItemStruct):

    Name = 'ItemStruct'
    Fields = InventoryItemStruct.Fields + (
        Enum3LowField('type', InventoryItemType, 0),
        FlagsField('properties', ItemProperty, 19),
        U8Field('effect_strength', 20),
        FlagsField('caused_conditions', ItemCondition, 21),
        EnumField('special_action', ItemSpecialAction, 27),
    )

class UsableNonItemStruct(InventoryItemStruct):

    Name = 'UsableNonItemStruct'
    Fields = InventoryItemStruct.Fields + (
        U8Field('attack_when_used', 18),
    )

class ToolStruct(UsableNonItemStruct):

    Name = 'ToolStruct'
    Fields = UsableNonItemStruct.Fields + (
        U8Field('attack_strength', 20),
        U8Field('hit_rate', 21),
    )

class EquipmentItemStruct(UsableNonItemStruct):

    Name = 'EquipmentItemStruct'
    Fields = UsableNonItemStruct.Fields + (
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
        Enum4LowField('evade_animation', EvadeAnimation, 27),
    )

class WeaponStruct(EquipmentItemStruct):

    Name = 'WeaponStruct'
    Fields = EquipmentItemStruct.Fields + (
        FlagsField('properties', WeaponProperty, 19),
        U8Field('battle_power', 20),
        U8Field('hit_rate', 21),
        Enum4HighField('special_attack', WeaponSpecialAttack, 27),
    )

class DefensiveEquipmentItemStruct(EquipmentItemStruct):

    Name = 'DefensiveEquipmentItemStruct'
    Fields = EquipmentItemStruct.Fields + (
        U8Field('physical_defense', 20),
        U8Field('magic_defense', 21),
        FlagsField('absorbed_elements', Element, 22),
        FlagsField('nullified_elements', Element, 23),
        FlagsField('weak_elements', Element, 24),
        FlagsField('caused_conditions2', Condition2, 25),
        U4HighField('evade', 26),
        U4LowField('magic_block', 26),
    )

class ArmorStruct(DefensiveEquipmentItemStruct):

    Name = 'ArmorStruct'

class ShieldStruct(DefensiveEquipmentItemStruct):

    Name = 'ShieldStruct'

class HatStruct(DefensiveEquipmentItemStruct):

    Name = 'HatStruct'

class RelicStruct(DefensiveEquipmentItemStruct):

    Name = 'RelicStruct'

class InventoryItemVariantStruct(VariantStruct):

    Name = 'InventoryItemVariantStruct'
    Size = 30
    VariantField = Enum4LowField('type', InventoryItemType, 0)
    Variants = {
        InventoryItemType.Tool: ToolStruct,
        InventoryItemType.Weapon: WeaponStruct,
        InventoryItemType.Armor: ArmorStruct,
        InventoryItemType.Shield: ShieldStruct,
        InventoryItemType.Hat: HatStruct,
        InventoryItemType.Relic: RelicStruct,
        InventoryItemType.Item: ItemStruct,
    }

class InventoryItemNameStructArray(StructArray):

    Name = 'InventoryItemNameStructArray'
    Count = 256
    Struct = InventoryItemNameStruct

class InventoryItemDataStructArray(StructArray):

    Name = 'InventoryItemDataStructArray'
    Count = 256
    Struct = InventoryItemVariantStruct
