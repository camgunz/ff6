from ff6.data import *
from ff6.typed_object import *

class InventoryItem(FF6Object):

    NameSize   = 13
    NameOffset = 0x0012B500
    DataSize   = 30
    DataOffset = 0x00185200

    def load(self):
        super().load()
        if self.type != self.ItemType:
            raise ValueError('%s: Expected type %s; got %s' % (
                self.name,
                self.ItemType,
                self.type
            ))

    @property
    def name_offset(self):
        return self.NameOffset + (self.NameSize * self.number)

    @property
    def data_offset(self):
        return self.DataOffset + (self.DataSize * self.number)

    def _build_fields(self):
        return super()._build_fields() + (
            Enum8Field(self, 'icon_type', EquipmentIconType, self.name_offset),
            BattleStrField(self, 'name', self.NameSize - 1,
                           self.name_offset + 1),
            Enum3LowField(self, 'type', InventoryItemType,
                          self.data_offset + 0),
            Flags5HighField(self, InventoryItemUsability, self.data_offset + 0),
            Flags8Field(self, Targeting, self.data_offset + 14, prefix='targets_'),
            U16Field(self, 'price', self.data_offset + 28),
        )

    def __str__(self):
        return '<%s (%d): %s>' % (self.type.name, self.number, self.name)

class Equipment(InventoryItem):

    def _build_fields(self):
        return super()._build_fields() + (
            Flags16Field(self, EquipInfo, self.data_offset + 1,
                         suffix='_equips'),
            U8Field(self, 'spell_learn_rate', self.data_offset + 3),
            U8Field(self, 'spell_learned', self.data_offset + 4),
            Flags8Field(self, FieldEffect, self.data_offset + 5),
            Flags8Field(self, Condition1, self.data_offset + 6,
                       prefix='protects_against_'),
            Flags8Field(self, Condition2, self.data_offset + 7,
                       prefix='protects_against_'),
            Flags8Field(self, Condition3, self.data_offset + 8,
                       prefix='causes_'),
            Flags8Field(self, StatusEffect1, self.data_offset + 9),
            Flags8Field(self, BattleEffect1, self.data_offset + 10),
            Flags8Field(self, StatusEffect2, self.data_offset + 11),
            Flags8Field(self, BattleEffect2, self.data_offset + 12),
            Flags8Field(self, BattleEffect3, self.data_offset + 13),
            Flags8Field(self, Element, self.data_offset + 15,
                       suffix='_elemental'),
            S4HighField(self, 'vigor', self.data_offset + 16),
            S4LowField(self, 'speed', self.data_offset + 16),
            S4HighField(self, 'stamina', self.data_offset + 17),
            S4LowField(self, 'magic_power', self.data_offset + 17),
            U8Field(self, 'attack_when_used', self.data_offset + 18),
            Enum4LowField(self, 'evade_animation', EvadeAnimation,
                          self.data_offset + 27),
        )

class DefensiveEquipment(Equipment):

    def _build_fields(self):
        return super()._build_fields() + (
            U8Field(self, 'physical_defense', self.data_offset + 20),
            U8Field(self, 'magic_defense', self.data_offset + 21),
            Flags8Field(self, Element, self.data_offset + 22,
                        prefix='absorbs_'),
            Flags8Field(self, Element, self.data_offset + 23,
                       prefix='nullifies_'),
            Flags8Field(self, Element, self.data_offset + 24,
                       prefix='weak_to_'),
            Flags8Field(self, Condition2, self.data_offset + 25,
                       prefix='causes_'),
            U4HighField(self, 'evade', self.data_offset + 26),
            U4LowField(self, 'magic_block', self.data_offset + 26),
        )

class Tool(InventoryItem):

    ItemType = InventoryItemType.Tool
    TypeName = ItemType.name

    def _build_fields(self):
        return super()._build_fields() + (
            U8Field(self, 'attack_when_used', self.data_offset + 18),
            U8Field(self, 'attack_strength', self.data_offset + 20),
            U8Field(self, 'hit_rate', self.data_offset + 21),
        )

class Weapon(Equipment):

    ItemType = InventoryItemType.Weapon
    TypeName = ItemType.name

    def _build_fields(self):
        return super()._build_fields() + (
            Flags8Field(self, WeaponProperty, self.data_offset + 19),
            U8Field(self, 'battle_power', self.data_offset + 20),
            U8Field(self, 'hit_rate', self.data_offset + 21),
            Enum4HighField(self, 'special_attack', WeaponSpecialAttack,
                           self.data_offset + 27),
        )

class Armor(DefensiveEquipment):
    ItemType = InventoryItemType.Armor
    TypeName = ItemType.name

class Shield(DefensiveEquipment):
    ItemType = InventoryItemType.Shield
    TypeName = ItemType.name

class Hat(DefensiveEquipment):
    ItemType = InventoryItemType.Hat
    TypeName = ItemType.name

class Relic(DefensiveEquipment):
    ItemType = InventoryItemType.Relic
    TypeName = ItemType.name

class Item(InventoryItem):

    ItemType = InventoryItemType.Item
    TypeName = ItemType.name

    def _build_fields(self):
        return super()._build_fields() + (
            Flags8Field(self, ItemProperty, self.data_offset + 19),
            U8Field(self, 'effect_strength', self.data_offset + 20),
            Flags8Field(self, Condition1, self.data_offset + 21,
                       prefix='causes_'),
            Flags8Field(self, Condition2, self.data_offset + 22,
                       prefix='causes_'),
            Flags8Field(self, Condition3, self.data_offset + 23,
                       prefix='causes_'),
            Flags8Field(self, Condition4, self.data_offset + 24,
                       prefix='causes_'),
            Enum8Field(self, 'special_action', ItemSpecialAction,
                       self.data_offset + 27)
        )

class Items(TypedObjectContainer):

    ObjectCount = 256
    Blanks = tuple()
    ObjectType = Item
    Name = 'Items'

    def _get_object_from_rom(self, rom, n):
        item_location = self.ObjectType.DataOffset + (n * self.ObjectType.DataSize)
        item_type = rom.read_byte(item_location) & 0x0F
        if item_type == InventoryItemType.Tool.value:
            return Tool(rom, n)
        if item_type == InventoryItemType.Weapon.value:
            return Weapon(rom, n)
        if item_type == InventoryItemType.Armor.value:
            return Armor(rom, n)
        if item_type == InventoryItemType.Shield.value:
            return Shield(rom, n)
        if item_type == InventoryItemType.Hat.value:
            return Hat(rom, n)
        if item_type == InventoryItemType.Relic.value:
            return Relic(rom, n)
        if item_type == InventoryItemType.Item.value:
            return Item(rom, n)
        raise ValueError('Unknown item type in ROM (got %s)' % (type))
