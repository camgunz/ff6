import struct

from ff6.data import *
from ff6.dte import DTE_BATTLE

def _8bit_signed(num):
    if num < 8:
        return num
    if num == 8:
        return 0
    if num > 7:
        return -(num % 8)

def _read_byte(data, location):
    return struct.unpack_from('B', data, location)[0]

def _read_signed_halfbyte(data, location):
    byte = struct.unpack_from('B', data, location)[0]
    return (_8bit_signed((byte & 0xF0) >> 4), _8bit_signed(byte & 0x0F))

def _read_short(data, location):
    return struct.unpack_from('<H', data, location)[0]

def _read_bytes(data, location, size):
    return struct.unpack_from('%ds' % (size), data, location)[0]

def _read_string(data, location, size):
    return struct.unpack_from('%ds' % (size), data, location)[0].decode('ascii')

def _read_dte_string(data, location, size):
    dte_indices = struct.unpack_from('%ds' % (size), data, location)[0]
    return ''.join([DTE_BATTLE[index] for index in dte_indices])

def _check_only_one(args, names):
    if len(list(filter(None, args))) > 1:
        msg = 'Only one of %s or %s may be given'
        raise ValueError(msg % (', '.join(names[:1]), names[-1]))

class InventoryItem:

    NameSize = 13
    DataSize = 30

    def __init__(self, number, name, type,
                       throwable,
                       usable_in_battle,
                       usable_in_field,
                       targets_single_ally_or_enemy,
                       targets_allies_or_enemies_only,
                       targets_all_allies_and_enemies,
                       targets_all_allies_or_all_enemies,
                       targets_only_default_selection,
                       targets_multiple,
                       targets_enemies_by_default,
                       targets_random, price):
        self.number = number
        self.name = name
        self.type = type
        self.throwable = throwable
        self.usable_in_battle = usable_in_battle
        self.usable_in_field = usable_in_field
        self.targets_single_ally_or_enemy = targets_single_ally_or_enemy
        self.targets_allies_or_enemies_only = targets_allies_or_enemies_only
        self.targets_all_allies_and_enemies = targets_all_allies_and_enemies
        self.targets_all_allies_or_all_enemies = targets_all_allies_or_all_enemies
        self.targets_only_default_selection = targets_only_default_selection
        self.targets_multiple = targets_multiple
        self.targets_enemies_by_default = targets_enemies_by_default
        self.targets_random = targets_random
        self.price = price

    def __str__(self):
        return '<%s: %s>' % (self.type.name, self.name)

class Equipment(InventoryItem):

    def __init__(self, number, name, type,
                       throwable,
                       usable_in_battle,
                       usable_in_field,
                       targets_single_ally_or_enemy,
                       targets_allies_or_enemies_only,
                       targets_all_allies_and_enemies,
                       targets_all_allies_or_all_enemies,
                       targets_only_default_selection,
                       targets_multiple,
                       targets_enemies_by_default,
                       targets_random,
                       price,
                       equippable_by_terra,
                       equippable_by_locke,
                       equippable_by_cyan,
                       equippable_by_shadow,
                       equippable_by_edgar,
                       equippable_by_sabin,
                       equippable_by_celes,
                       equippable_by_strago,
                       equippable_by_relm,
                       equippable_by_setzer,
                       equippable_by_mog,
                       equippable_by_gau,
                       equippable_by_gogo,
                       equippable_by_umaro,
                       equippable_by_imp,
                       spell_learn_rate,
                       spell_learned,
                       reduces_enemy_attacks,
                       prevents_enemy_attacks,
                       doubles_walking_speed,
                       cures_one_hp_per_step,
                       protects_against_dark,
                       protects_against_zombie,
                       protects_against_poison,
                       protects_against_magitek,
                       protects_against_vanish,
                       protects_against_imp,
                       protects_against_petrify,
                       protects_against_death,
                       protects_against_condemned,
                       protects_against_kneeling,
                       protects_against_blink,
                       protects_against_silence,
                       protects_against_berserk,
                       protects_against_confusion,
                       protects_against_hp_drain,
                       protects_against_sleep,
                       raises_attack_damage,
                       raises_magic_damage,
                       raises_hp_one_quarter,
                       raises_hp_one_half,
                       raises_hp_one_eighth,
                       raises_mp_one_quarter,
                       raises_mp_one_half,
                       raises_mp_one_eighth,
                       enables_jump,
                       enables_x_magic,
                       enables_control,
                       enables_gp_rain,
                       enables_capture,
                       forces_continuous_jump,
                       increases_steal_rate,
                       enables_perfect_hit_rate,
                       halves_mp_consumption,
                       sets_mp_consumption_to_one,
                       raises_vigor,
                       enables_x_fight,
                       randomly_counter_attacks,
                       increases_evade_chance,
                       allows_two_hands,
                       allows_dual_wield,
                       enables_heavy_armor,
                       protects_allies,
                       casts_shell_on_low_hp,
                       casts_safe_on_low_hp,
                       casts_reflect_on_low_hp,
                       doubles_experience,
                       doubles_gold,
                       makes_body_cold,
                       fire_elemental,
                       ice_elemental,
                       lightning_elemental,
                       poison_elemental,
                       wind_elemental,
                       pearl_elemental,
                       earth_elemental,
                       water_elemental,
                       vigor,
                       speed,
                       stamina,
                       magic_power,
                       attack_when_used,
                       evade,
                       magic_block):
        super().__init__(number, name, type,
                         throwable,
                         usable_in_battle,
                         usable_in_field,
                         targets_single_ally_or_enemy,
                         targets_allies_or_enemies_only,
                         targets_all_allies_and_enemies,
                         targets_all_allies_or_all_enemies,
                         targets_only_default_selection,
                         targets_multiple,
                         targets_enemies_by_default,
                         targets_random, price)
        self.equippable_by_terra = equippable_by_terra
        self.equippable_by_locke = equippable_by_locke
        self.equippable_by_cyan = equippable_by_cyan
        self.equippable_by_shadow = equippable_by_shadow
        self.equippable_by_edgar = equippable_by_edgar
        self.equippable_by_sabin = equippable_by_sabin
        self.equippable_by_celes = equippable_by_celes
        self.equippable_by_strago = equippable_by_strago
        self.equippable_by_relm = equippable_by_relm
        self.equippable_by_setzer = equippable_by_setzer
        self.equippable_by_mog = equippable_by_mog
        self.equippable_by_gau = equippable_by_gau
        self.equippable_by_gogo = equippable_by_gogo
        self.equippable_by_umaro = equippable_by_umaro
        self.equippable_by_imp = equippable_by_imp
        self.spell_learn_rate = spell_learn_rate
        self.spell_learned = spell_learned
        self.reduces_enemy_attacks = reduces_enemy_attacks
        self.prevents_enemy_attacks = prevents_enemy_attacks
        self.doubles_walking_speed = doubles_walking_speed
        self.cures_one_hp_per_step = cures_one_hp_per_step
        self.protects_against_dark = protects_against_dark
        self.protects_against_zombie = protects_against_zombie
        self.protects_against_poison = protects_against_poison
        self.protects_against_magitek = protects_against_magitek
        self.protects_against_vanish = protects_against_vanish
        self.protects_against_imp = protects_against_imp
        self.protects_against_petrify = protects_against_petrify
        self.protects_against_death = protects_against_death
        self.protects_against_condemned = protects_against_condemned
        self.protects_against_kneeling = protects_against_kneeling
        self.protects_against_blink = protects_against_blink
        self.protects_against_silence = protects_against_silence
        self.protects_against_berserk = protects_against_berserk
        self.protects_against_confusion = protects_against_confusion
        self.protects_against_hp_drain = protects_against_hp_drain
        self.protects_against_sleep = protects_against_sleep
        self.raises_attack_damage = raises_attack_damage
        self.raises_magic_damage = raises_magic_damage
        self.raises_hp_one_quarter = raises_hp_one_quarter
        self.raises_hp_one_half = raises_hp_one_half
        self.raises_hp_one_eighth = raises_hp_one_eighth
        self.raises_mp_one_quarter = raises_mp_one_quarter
        self.raises_mp_one_half = raises_mp_one_half
        self.raises_mp_one_eighth = raises_mp_one_eighth
        self.enables_jump = enables_jump
        self.enables_x_magic = enables_x_magic
        self.enables_control = enables_control
        self.enables_gp_rain = enables_gp_rain
        self.enables_capture = enables_capture
        self.forces_continuous_jump = forces_continuous_jump
        self.increases_steal_rate = increases_steal_rate
        self.enables_perfect_hit_rate = enables_perfect_hit_rate
        self.halves_mp_consumption = halves_mp_consumption
        self.sets_mp_consumption_to_one = sets_mp_consumption_to_one
        self.raises_vigor = raises_vigor
        self.enables_x_fight = enables_x_fight
        self.randomly_counter_attacks = randomly_counter_attacks
        self.increases_evade_chance = increases_evade_chance
        self.allows_two_hands = allows_two_hands
        self.allows_dual_wield = allows_dual_wield
        self.enables_heavy_armor = enables_heavy_armor
        self.protects_allies = protects_allies
        self.casts_shell_on_low_hp = casts_shell_on_low_hp
        self.casts_safe_on_low_hp = casts_safe_on_low_hp
        self.casts_reflect_on_low_hp = casts_reflect_on_low_hp
        self.doubles_experience = doubles_experience
        self.doubles_gold = doubles_gold
        self.makes_body_cold = makes_body_cold
        self.fire_elemental = fire_elemental
        self.ice_elemental = ice_elemental
        self.lightning_elemental = lightning_elemental
        self.poison_elemental = poison_elemental
        self.wind_elemental = wind_elemental
        self.pearl_elemental = pearl_elemental
        self.earth_elemental = earth_elemental
        self.water_elemental = water_elemental
        self.vigor = vigor
        self.speed = speed
        self.stamina = stamina
        self.magic_power = magic_power
        self.attack_when_used = attack_when_used
        self.evade = evade
        self.magic_block = magic_block

class DefensiveEquipment(Equipment):

    def __init__(self, number, name,
                       throwable,
                       usable_in_battle,
                       usable_in_field,
                       targets_single_ally_or_enemy,
                       targets_allies_or_enemies_only,
                       targets_all_allies_and_enemies,
                       targets_all_allies_or_all_enemies,
                       targets_only_default_selection,
                       targets_multiple,
                       targets_enemies_by_default,
                       targets_random,
                       price,
                       equippable_by_terra,
                       equippable_by_locke,
                       equippable_by_cyan,
                       equippable_by_shadow,
                       equippable_by_edgar,
                       equippable_by_sabin,
                       equippable_by_celes,
                       equippable_by_strago,
                       equippable_by_relm,
                       equippable_by_setzer,
                       equippable_by_mog,
                       equippable_by_gau,
                       equippable_by_gogo,
                       equippable_by_umaro,
                       equippable_by_imp,
                       spell_learn_rate,
                       spell_learned,
                       reduces_enemy_attacks,
                       prevents_enemy_attacks,
                       doubles_walking_speed,
                       cures_one_hp_per_step,
                       protects_against_dark,
                       protects_against_zombie,
                       protects_against_poison,
                       protects_against_magitek,
                       protects_against_vanish,
                       protects_against_imp,
                       protects_against_petrify,
                       protects_against_death,
                       protects_against_condemned,
                       protects_against_kneeling,
                       protects_against_blink,
                       protects_against_silence,
                       protects_against_berserk,
                       protects_against_confusion,
                       protects_against_hp_drain,
                       protects_against_sleep,
                       causes_float,
                       causes_regen,
                       causes_slow,
                       causes_haste,
                       causes_stop,
                       causes_shell,
                       causes_safe,
                       causes_reflect,
                       raises_attack_damage,
                       raises_magic_damage,
                       raises_hp_one_quarter,
                       raises_hp_one_half,
                       raises_hp_one_eighth,
                       raises_mp_one_quarter,
                       raises_mp_one_half,
                       raises_mp_one_eighth,
                       enables_jump,
                       enables_x_magic,
                       enables_control,
                       enables_gp_rain,
                       enables_capture,
                       forces_continuous_jump,
                       increases_steal_rate,
                       enables_perfect_hit_rate,
                       halves_mp_consumption,
                       sets_mp_consumption_to_one,
                       raises_vigor,
                       enables_x_fight,
                       randomly_counter_attacks,
                       increases_evade_chance,
                       allows_two_hands,
                       allows_dual_wield,
                       enables_heavy_armor,
                       protects_allies,
                       casts_shell_on_low_hp,
                       casts_safe_on_low_hp,
                       casts_reflect_on_low_hp,
                       doubles_experience,
                       doubles_gold,
                       makes_body_cold,
                       fire_elemental,
                       ice_elemental,
                       lightning_elemental,
                       poison_elemental,
                       wind_elemental,
                       pearl_elemental,
                       earth_elemental,
                       water_elemental,
                       vigor,
                       speed,
                       stamina,
                       magic_power,
                       attack_when_used,
                       physical_defense,
                       magic_defense,
                       absorbs_fire,
                       absorbs_ice,
                       absorbs_lightning,
                       absorbs_poison,
                       absorbs_wind,
                       absorbs_pearl,
                       absorbs_earth,
                       absorbs_water,
                       nullifies_fire,
                       nullifies_ice,
                       nullifies_lightning,
                       nullifies_poison,
                       nullifies_wind,
                       nullifies_pearl,
                       nullifies_earth,
                       nullifies_water,
                       weak_to_fire,
                       weak_to_ice,
                       weak_to_lightning,
                       weak_to_poison,
                       weak_to_wind,
                       weak_to_pearl,
                       weak_to_earth,
                       weak_to_water,
                       causes_condemned,
                       causes_kneeling,
                       causes_blink,
                       causes_silence,
                       causes_berserk,
                       causes_confusion,
                       causes_hp_drain,
                       causes_sleep,
                       evade,
                       magic_block):
        super().__init__(number, name, self._InventoryItemType,
                         throwable,
                         usable_in_battle,
                         usable_in_field,
                         targets_single_ally_or_enemy,
                         targets_allies_or_enemies_only,
                         targets_all_allies_and_enemies,
                         targets_all_allies_or_all_enemies,
                         targets_only_default_selection,
                         targets_multiple,
                         targets_enemies_by_default,
                         targets_random,
                         price,
                         equippable_by_terra,
                         equippable_by_locke,
                         equippable_by_cyan,
                         equippable_by_shadow,
                         equippable_by_edgar,
                         equippable_by_sabin,
                         equippable_by_celes,
                         equippable_by_strago,
                         equippable_by_relm,
                         equippable_by_setzer,
                         equippable_by_mog,
                         equippable_by_gau,
                         equippable_by_gogo,
                         equippable_by_umaro,
                         equippable_by_imp,
                         spell_learn_rate,
                         spell_learned,
                         reduces_enemy_attacks,
                         prevents_enemy_attacks,
                         doubles_walking_speed,
                         cures_one_hp_per_step,
                         protects_against_dark,
                         protects_against_zombie,
                         protects_against_poison,
                         protects_against_magitek,
                         protects_against_vanish,
                         protects_against_imp,
                         protects_against_petrify,
                         protects_against_death,
                         protects_against_condemned,
                         protects_against_kneeling,
                         protects_against_blink,
                         protects_against_silence,
                         protects_against_berserk,
                         protects_against_confusion,
                         protects_against_hp_drain,
                         protects_against_sleep,
                         raises_attack_damage,
                         raises_magic_damage,
                         raises_hp_one_quarter,
                         raises_hp_one_half,
                         raises_hp_one_eighth,
                         raises_mp_one_quarter,
                         raises_mp_one_half,
                         raises_mp_one_eighth,
                         enables_jump,
                         enables_x_magic,
                         enables_control,
                         enables_gp_rain,
                         enables_capture,
                         forces_continuous_jump,
                         increases_steal_rate,
                         enables_perfect_hit_rate,
                         halves_mp_consumption,
                         sets_mp_consumption_to_one,
                         raises_vigor,
                         enables_x_fight,
                         randomly_counter_attacks,
                         increases_evade_chance,
                         allows_two_hands,
                         allows_dual_wield,
                         enables_heavy_armor,
                         protects_allies,
                         casts_shell_on_low_hp,
                         casts_safe_on_low_hp,
                         casts_reflect_on_low_hp,
                         doubles_experience,
                         doubles_gold,
                         makes_body_cold,
                         fire_elemental,
                         ice_elemental,
                         lightning_elemental,
                         poison_elemental,
                         wind_elemental,
                         pearl_elemental,
                         earth_elemental,
                         water_elemental,
                         vigor,
                         speed,
                         stamina,
                         magic_power,
                         attack_when_used,
                         evade,
                         magic_block)
        self.physical_defense = physical_defense
        self.magic_defense = magic_defense
        self.absorbs_fire = absorbs_fire
        self.absorbs_ice = absorbs_ice
        self.absorbs_lightning = absorbs_lightning
        self.absorbs_poison = absorbs_poison
        self.absorbs_wind = absorbs_wind
        self.absorbs_pearl = absorbs_pearl
        self.absorbs_earth = absorbs_earth
        self.absorbs_water = absorbs_water
        self.nullifies_fire = nullifies_fire
        self.nullifies_ice = nullifies_ice
        self.nullifies_lightning = nullifies_lightning
        self.nullifies_poison = nullifies_poison
        self.nullifies_wind = nullifies_wind
        self.nullifies_pearl = nullifies_pearl
        self.nullifies_earth = nullifies_earth
        self.nullifies_water = nullifies_water
        self.weak_to_fire = weak_to_fire
        self.weak_to_ice = weak_to_ice
        self.weak_to_lightning = weak_to_lightning
        self.weak_to_poison = weak_to_poison
        self.weak_to_wind = weak_to_wind
        self.weak_to_pearl = weak_to_pearl
        self.weak_to_earth = weak_to_earth
        self.weak_to_water = weak_to_water
        self.causes_condemned = causes_condemned
        self.causes_kneeling = causes_kneeling
        self.causes_blink = causes_blink
        self.causes_silence = causes_silence
        self.causes_berserk = causes_berserk
        self.causes_confusion = causes_confusion
        self.causes_hp_drain = causes_hp_drain
        self.causes_sleep = causes_sleep

    @classmethod
    def from_rom(cls, rom, number):
        name_offset = cls.NameSize * number
        name_start = rom.ItemNamesOffset+name_offset
        name = _read_dte_string(rom.data, name_start, 13)
        data_offset = cls.DataSize * number
        data_start = rom.ItemDataOffset+data_offset
        type = _read_byte(rom.data, data_start + 0)
        usability = type & 0xF0
        type = type & 0x0F
        equippable_chars = _read_short(rom.data, data_start + 1)
        spell_learn_rate = _read_byte(rom.data, data_start + 3)
        spell_learned = _read_byte(rom.data, data_start + 4)
        field_effects = _read_byte(rom.data, data_start + 5)
        cond_protection1 = _read_byte(rom.data, data_start + 6)
        cond_protection2 = _read_byte(rom.data, data_start + 7)
        cond_caused3 = _read_byte(rom.data, data_start + 8)
        status_effects1 = _read_byte(rom.data, data_start + 9)
        battle_effects1 = _read_byte(rom.data, data_start + 10)
        status_effects2 = _read_byte(rom.data, data_start + 11)
        battle_effects2 = _read_byte(rom.data, data_start + 12)
        battle_effects3 = _read_byte(rom.data, data_start + 13)
        targeting = _read_byte(rom.data, data_start + 14)
        elements = _read_byte(rom.data, data_start + 15)
        vigor_and_speed = _read_signed_halfbyte(rom.data, data_start + 16)
        stamina_and_mpow = _read_signed_halfbyte(rom.data, data_start + 17)
        attack_when_used = _read_byte(rom.data, data_start + 18)
        physical_defense = _read_byte(rom.data, data_start + 20)
        magic_defense = _read_byte(rom.data, data_start + 21)
        absorbed_elements = _read_byte(rom.data, data_start + 22)
        nullified_elements = _read_byte(rom.data, data_start + 23)
        weak_elements = _read_byte(rom.data, data_start + 24)
        cond_caused2 = _read_byte(rom.data, data_start + 25)
        evade_and_mblock = _read_signed_halfbyte(rom.data, data_start + 26)
        price = _read_short(rom.data, data_start + 28)
        attributes = {}
        if type != cls._InventoryItemType.value:
            msg = 'Invalid item type in ROM (got %s, expected %s)'
            raise ValueError(msg % (type, cls._InventoryItemType))
        attributes['number'] = number
        attributes['name'] = name
        attributes['spell_learn_rate'] = spell_learn_rate
        attributes['spell_learned'] = spell_learned
        attributes['attack_when_used'] = attack_when_used
        attributes['physical_defense'] = physical_defense
        attributes['magic_defense'] = magic_defense
        attributes['vigor'], attributes['speed'] = vigor_and_speed
        attributes['stamina'], attributes['magic_power'] = stamina_and_mpow
        attributes['evade'], attributes['magic_block'] = evade_and_mblock
        attributes['price'] = price
        enum_params = [
            ('usability', usability, InventoryItemUsability),
            ('equippable chars', equippable_chars, Character,
             'equippable_by_'),
            ('field effects', field_effects, FieldEffect),
            ('protected conditions 1', cond_protection1, Condition1,
             'protects_against_'),
            ('protected conditions 2', cond_protection2, Condition2,
             'protects_against_'),
            ('caused conditions 3', cond_caused3, Condition3, 'causes_'),
            ('status effects 1', status_effects1, StatusEffect1),
            ('battle effects 1', battle_effects1, BattleEffect1),
            ('status effects 2', status_effects2, StatusEffect2),
            ('battle effects 2', battle_effects2, BattleEffect2),
            ('battle effects 3', battle_effects3, BattleEffect3),
            ('targeting', targeting, Targeting, 'targets_'),
            ('elements', elements, Element, None, '_elemental'),
            ('absorbed elements', absorbed_elements, Element, 'absorbs_'),
            ('nullified elements', nullified_elements, Element, 'nullifies_'),
            ('weak elements', weak_elements, Element, 'weak_to_'),
            ('caused conditions 2', cond_caused2, Condition2, 'causes_'),
        ]
        for args in enum_params:
            attributes.update(get_matching_values_as_params(*args))
        attributes['causes_float'] = attributes['causes_dance_or_float']
        del attributes['causes_dance_or_float']
        return cls(**attributes)

class Tool(InventoryItem):

    def __init__(self, number, name,
                       throwable,
                       usable_in_battle,
                       usable_in_field,
                       targets_single_ally_or_enemy,
                       targets_allies_or_enemies_only,
                       targets_all_allies_and_enemies,
                       targets_all_allies_or_all_enemies,
                       targets_only_default_selection,
                       targets_multiple,
                       targets_enemies_by_default,
                       targets_random,
                       attack_when_used,
                       attack_strength,
                       hit_rate,
                       price):
        super().__init__(number, name, InventoryItemType.Tool,
                         throwable,
                         usable_in_battle,
                         usable_in_field,
                         targets_single_ally_or_enemy,
                         targets_allies_or_enemies_only,
                         targets_all_allies_and_enemies,
                         targets_all_allies_or_all_enemies,
                         targets_only_default_selection,
                         targets_multiple,
                         targets_enemies_by_default,
                         targets_random,
                         price)
        self.attack_when_used = attack_when_used
        self.attack_strength = attack_strength
        self.hit_rate = hit_rate

    @classmethod
    def from_rom(cls, rom, number):
        name_offset = cls.NameSize * number
        name_start = rom.ItemNamesOffset+name_offset
        name = _read_dte_string(rom.data, name_start, 13)
        data_offset = cls.DataSize * number
        data_start = rom.ItemDataOffset+data_offset
        type = _read_byte(rom.data, data_start + 0)
        usability = type & 0xF0
        type = type & 0x0F
        targeting = _read_byte(rom.data, data_start + 14)
        attack_when_used = _read_byte(rom.data, data_start + 18)
        attack_strength = _read_byte(rom.data, data_start + 20)
        hit_rate = _read_byte(rom.data, data_start + 21)
        price = _read_short(rom.data, data_start + 28)
        attributes = {}
        if type != InventoryItemType.Tool.value:
            msg = 'Invalid item type in ROM (got %s, expected %s)'
            raise ValueError(msg % (type, InventoryItemType.Tool))
        attributes['number'] = number
        attributes['name'] = name
        attributes['attack_when_used'] = attack_when_used
        attributes['attack_strength'] = attack_strength
        attributes['hit_rate'] = hit_rate
        attributes['price'] = price
        enum_params = [
            ('usability', usability, InventoryItemUsability),
            ('targeting', targeting, Targeting, 'targets_'),
        ]
        for args in enum_params:
            attributes.update(get_matching_values_as_params(*args))
        return cls(**attributes)

class Weapon(Equipment):

    def __init__(self, number, name, type,
                       throwable,
                       usable_in_battle,
                       usable_in_field,
                       targets_single_ally_or_enemy,
                       targets_allies_or_enemies_only,
                       targets_all_allies_and_enemies,
                       targets_all_allies_or_all_enemies,
                       targets_only_default_selection,
                       targets_multiple,
                       targets_enemies_by_default,
                       targets_random,
                       price,
                       equippable_by_terra,
                       equippable_by_locke,
                       equippable_by_cyan,
                       equippable_by_shadow,
                       equippable_by_edgar,
                       equippable_by_sabin,
                       equippable_by_celes,
                       equippable_by_strago,
                       equippable_by_relm,
                       equippable_by_setzer,
                       equippable_by_mog,
                       equippable_by_gau,
                       equippable_by_gogo,
                       equippable_by_umaro,
                       equippable_by_imp,
                       spell_learn_rate,
                       spell_learned,
                       reduces_enemy_attacks,
                       prevents_enemy_attacks,
                       doubles_walking_speed,
                       cures_one_hp_per_step,
                       protects_against_dark,
                       protects_against_zombie,
                       protects_against_poison,
                       protects_against_magitek,
                       protects_against_vanish,
                       protects_against_imp,
                       protects_against_petrify,
                       protects_against_death,
                       protects_against_condemned,
                       protects_against_kneeling,
                       protects_against_blink,
                       protects_against_silence,
                       protects_against_berserk,
                       protects_against_confusion,
                       protects_against_hp_drain,
                       protects_against_sleep,
                       causes_float,
                       causes_regen,
                       causes_slow,
                       causes_haste,
                       causes_stop,
                       causes_shell,
                       causes_safe,
                       causes_reflect,
                       raises_attack_damage,
                       raises_magic_damage,
                       raises_hp_one_quarter,
                       raises_hp_one_half,
                       raises_hp_one_eighth,
                       raises_mp_one_quarter,
                       raises_mp_one_half,
                       raises_mp_one_eighth,
                       enables_jump,
                       enables_x_magic,
                       enables_control,
                       enables_gp_rain,
                       enables_capture,
                       forces_continuous_jump,
                       increases_steal_rate,
                       enables_perfect_hit_rate,
                       halves_mp_consumption,
                       sets_mp_consumption_to_one,
                       raises_vigor,
                       enables_x_fight,
                       randomly_counter_attacks,
                       increases_evade_chance,
                       allows_two_hands,
                       allows_dual_wield,
                       enables_heavy_armor,
                       protects_allies,
                       casts_shell_on_low_hp,
                       casts_safe_on_low_hp,
                       casts_reflect_on_low_hp,
                       doubles_experience,
                       doubles_gold,
                       makes_body_cold,
                       fire_elemental,
                       ice_elemental,
                       lightning_elemental,
                       poison_elemental,
                       wind_elemental,
                       pearl_elemental,
                       earth_elemental,
                       water_elemental,
                       vigor,
                       speed,
                       stamina,
                       magic_power,
                       attack_when_used,
                       usable_with_bushido,
                       same_damage_from_back_row,
                       usable_with_two_hands,
                       usable_with_runic,
                       battle_power,
                       hit_rate,
                       evade,
                       magic_block,
                       steals,
                       attack_power_increases_as_hp_increases,
                       kills_with_x,
                       doubles_human_damage,
                       drains_hp,
                       drains_mp,
                       affects_mp,
                       is_dice,
                       attack_power_increases_as_hp_decreases,
                       has_wind_attack,
                       recovers_hp,
                       kills,
                       uses_mp_for_critical,
                       uses_more_mp_for_critical):
        super().__init__(number, name, InventoryItemType.Weapon,
                         throwable,
                         usable_in_battle,
                         usable_in_field,
                         targets_single_ally_or_enemy,
                         targets_allies_or_enemies_only,
                         targets_all_allies_and_enemies,
                         targets_all_allies_or_all_enemies,
                         targets_only_default_selection,
                         targets_multiple,
                         targets_enemies_by_default,
                         targets_random,
                         price,
                         equippable_by_terra,
                         equippable_by_locke,
                         equippable_by_cyan,
                         equippable_by_shadow,
                         equippable_by_edgar,
                         equippable_by_sabin,
                         equippable_by_celes,
                         equippable_by_strago,
                         equippable_by_relm,
                         equippable_by_setzer,
                         equippable_by_mog,
                         equippable_by_gau,
                         equippable_by_gogo,
                         equippable_by_umaro,
                         equippable_by_imp,
                         spell_learn_rate,
                         spell_learned,
                         reduces_enemy_attacks,
                         prevents_enemy_attacks,
                         doubles_walking_speed,
                         cures_one_hp_per_step,
                         protects_against_dark,
                         protects_against_zombie,
                         protects_against_poison,
                         protects_against_magitek,
                         protects_against_vanish,
                         protects_against_imp,
                         protects_against_petrify,
                         protects_against_death,
                         protects_against_condemned,
                         protects_against_kneeling,
                         protects_against_blink,
                         protects_against_silence,
                         protects_against_berserk,
                         protects_against_confusion,
                         protects_against_hp_drain,
                         protects_against_sleep,
                         raises_attack_damage,
                         raises_magic_damage,
                         raises_hp_one_quarter,
                         raises_hp_one_half,
                         raises_hp_one_eighth,
                         raises_mp_one_quarter,
                         raises_mp_one_half,
                         raises_mp_one_eighth,
                         enables_jump,
                         enables_x_magic,
                         enables_control,
                         enables_gp_rain,
                         enables_capture,
                         forces_continuous_jump,
                         increases_steal_rate,
                         enables_perfect_hit_rate,
                         halves_mp_consumption,
                         sets_mp_consumption_to_one,
                         raises_vigor,
                         enables_x_fight,
                         randomly_counter_attacks,
                         increases_evade_chance,
                         allows_two_hands,
                         allows_dual_wield,
                         enables_heavy_armor,
                         protects_allies,
                         casts_shell_on_low_hp,
                         casts_safe_on_low_hp,
                         casts_reflect_on_low_hp,
                         doubles_experience,
                         doubles_gold,
                         makes_body_cold,
                         fire_elemental,
                         ice_elemental,
                         lightning_elemental,
                         poison_elemental,
                         wind_elemental,
                         pearl_elemental,
                         earth_elemental,
                         water_elemental,
                         vigor,
                         speed,
                         stamina,
                         magic_power,
                         attack_when_used,
                         evade,
                         magic_block)
        self.usable_with_bushido = usable_with_bushido
        self.same_damage_from_back_row = same_damage_from_back_row
        self.usable_with_two_hands = usable_with_two_hands
        self.usable_with_runic = usable_with_runic
        self.battle_power = battle_power
        _check_only_one([steals,
                         attack_power_increases_as_hp_increases,
                         kills_with_x,
                         doubles_human_damage,
                         drains_hp,
                         drains_mp,
                         affects_mp,
                         is_dice,
                         attack_power_increases_as_hp_decreases,
                         has_wind_attack,
                         recovers_hp,
                         kills,
                         uses_mp_for_critical,
                         uses_more_mp_for_critical],
                        ['steals',
                         'attack_power_increases_as_hp_increases',
                         'kills_with_x',
                         'doubles_human_damage',
                         'drains_hp',
                         'drains_mp',
                         'affects_mp',
                         'is_dice',
                         'attack_power_increases_as_hp_decreases',
                         'has_wind_attack',
                         'recovers_hp',
                         'kills',
                         'uses_mp_for_critical',
                         'uses_more_mp_for_critical'])
        self.steals = steals
        self.attack_power_increases_as_hp_increases = \
            attack_power_increases_as_hp_increases
        self.kills_with_x = kills_with_x
        self.doubles_human_damage = doubles_human_damage
        self.drains_hp = drains_hp
        self.drains_mp = drains_mp
        self.affects_mp = affects_mp
        self.is_dice = is_dice
        self.attack_power_increases_as_hp_decreases = \
            attack_power_increases_as_hp_decreases
        self.has_wind_attack = has_wind_attack
        self.recovers_hp = recovers_hp
        self.kills = kills
        self.uses_mp_for_critical = uses_mp_for_critical
        self.uses_more_mp_for_critical = uses_more_mp_for_critical

    @classmethod
    def from_rom(cls, rom, number):
        name_offset = cls.NameSize * number
        name_start = rom.ItemNamesOffset+name_offset
        name = _read_dte_string(rom.data, name_start, 13)
        data_offset = cls.DataSize * number
        data_start = rom.ItemDataOffset+data_offset
        type = _read_byte(rom.data, data_start + 0)
        usability = type & 0xF0
        type = type & 0x0F
        equippable_chars = _read_short(rom.data, data_start + 1)
        spell_learn_rate = _read_byte(rom.data, data_start + 3)
        spell_learned = _read_byte(rom.data, data_start + 4)
        field_effects = _read_byte(rom.data, data_start + 5)
        cond_protection1 = _read_byte(rom.data, data_start + 6)
        cond_protection2 = _read_byte(rom.data, data_start + 7)
        cond_caused3 = _read_byte(rom.data, data_start + 8)
        status_effects1 = _read_byte(rom.data, data_start + 9)
        battle_effects1 = _read_byte(rom.data, data_start + 10)
        status_effects2 = _read_byte(rom.data, data_start + 11)
        battle_effects2 = _read_byte(rom.data, data_start + 12)
        battle_effects3 = _read_byte(rom.data, data_start + 13)
        targeting = _read_byte(rom.data, data_start + 14)
        elements = _read_byte(rom.data, data_start + 15)
        vigor_and_speed = _read_signed_halfbyte(rom.data, data_start + 16)
        stamina_and_mpow = _read_signed_halfbyte(rom.data, data_start + 17)
        attack_when_used = _read_byte(rom.data, data_start + 18)
        weapon_properties = _read_byte(rom.data, data_start + 19)
        battle_power = _read_byte(rom.data, data_start + 20)
        hit_rate = _read_byte(rom.data, data_start + 21)
        evade_and_mblock = _read_signed_halfbyte(rom.data, data_start + 26)
        special_attack = _read_byte(rom.data, data_start + 27)
        price = _read_short(rom.data, data_start + 28)
        attributes = {}
        if type != InventoryItemType.Weapon.value:
            msg = 'Invalid item type in ROM (got %s, expected %s)'
            raise ValueError(msg % (type, InventoryItemType.Weapon))
        attributes['number'] = number
        attributes['name'] = name
        attributes['type'] = type
        attributes['spell_learn_rate'] = spell_learn_rate
        attributes['spell_learned'] = spell_learned
        attributes['attack_when_used'] = attack_when_used
        attributes['battle_power'] = battle_power
        attributes['hit_rate'] = hit_rate
        attributes['vigor'], attributes['speed'] = vigor_and_speed
        attributes['stamina'], attributes['magic_power'] = stamina_and_mpow
        attributes['evade'], attributes['magic_block'] = evade_and_mblock
        attributes['price'] = price
        enum_params = [
            ('usability', usability, InventoryItemUsability),
            ('equippable chars', equippable_chars, Character,
             'equippable_by_'),
            ('field effects', field_effects, FieldEffect),
            ('protected conditions 1', cond_protection1, Condition1,
             'protects_against_'),
            ('protected conditions 2', cond_protection2, Condition2,
             'protects_against_'),
            ('caused conditions 3', cond_caused3, Condition3, 'causes_'),
            ('status effects 1', status_effects1, StatusEffect1),
            ('battle effects 1', battle_effects1, BattleEffect1),
            ('status effects 2', status_effects2, StatusEffect2),
            ('battle effects 2', battle_effects2, BattleEffect2),
            ('battle effects 3', battle_effects3, BattleEffect3),
            ('targeting', targeting, Targeting, 'targets_'),
            ('elements', elements, Element, None, '_elemental'),
            ('weapon properties', weapon_properties, WeaponProperty),
        ]
        for args in enum_params:
            attributes.update(get_matching_values_as_params(*args))
        attributes['causes_float'] = attributes['causes_dance_or_float']
        del attributes['causes_dance_or_float']
        attributes.update(get_matching_values_as_params_limit_one(
            special_attack,
            SpecialAttack,
            ignores=[SpecialAttack.NoSpecialAttack.value]))
        return cls(**attributes)

class Armor(DefensiveEquipment):

    _InventoryItemType = InventoryItemType.Armor

class Shield(DefensiveEquipment):

    _InventoryItemType = InventoryItemType.Shield

class Hat(DefensiveEquipment):

    _InventoryItemType = InventoryItemType.Hat

class Relic(DefensiveEquipment):

    _InventoryItemType = InventoryItemType.Relic

class Item(InventoryItem):

    def __init__(self, number, name, type,
                       throwable,
                       usable_in_battle,
                       usable_in_field,
                       targets_single_ally_or_enemy,
                       targets_allies_or_enemies_only,
                       targets_all_allies_and_enemies,
                       targets_all_allies_or_all_enemies,
                       targets_only_default_selection,
                       targets_multiple,
                       targets_enemies_by_default,
                       targets_random,
                       price,
                       restores_hp,
                       restores_mp,
                       removes_status_conditions,
                       causes_damage,
                       effect_is_proportionate,
                       effect_strength,
                       causes_dark,
                       causes_zombie,
                       causes_poison,
                       causes_magitek,
                       causes_vanish,
                       causes_imp,
                       causes_petrify,
                       causes_death,
                       causes_condemned,
                       causes_kneeling,
                       causes_blink,
                       causes_silence,
                       causes_berserk,
                       causes_confusion,
                       causes_hp_drain,
                       causes_sleep,
                       causes_dance_or_float,
                       causes_regen,
                       causes_slow,
                       causes_haste,
                       causes_stop,
                       causes_shell,
                       causes_safe,
                       causes_reflect,
                       causes_rage,
                       causes_frozen,
                       causes_protection_from_death,
                       causes_morph,
                       causes_casting,
                       causes_removed,
                       causes_defended_by_interceptor,
                       causes_float,
                       summons_random_esper,
                       is_super_ball,
                       removes_character_from_battle,
                       is_elixir,
                       removes_all_characters_from_battle,
                       attracts_gau):
        super().__init__(number, name, type,
                               throwable,
                               usable_in_battle,
                               usable_in_field,
                         targets_single_ally_or_enemy,
                         targets_allies_or_enemies_only,
                         targets_all_allies_and_enemies,
                         targets_all_allies_or_all_enemies,
                         targets_only_default_selection,
                         targets_multiple,
                         targets_enemies_by_default,
                         targets_random,
                         price)
        self.restores_hp = restores_hp
        self.restores_mp = restores_mp
        self.removes_status_conditions = removes_status_conditions
        self.causes_damage = causes_damage
        self.effect_is_proportionate = effect_is_proportionate
        self.effect_strength = effect_strength
        _check_only_one([summons_random_esper,
                         is_super_ball,
                         removes_character_from_battle,
                         is_elixir,
                         removes_all_characters_from_battle,
                         attracts_gau],
                        ['summons_random_esper',
                         'is_super_ball',
                         'removes_character_from_battle',
                         'is_elixir',
                         'removes_all_characters_from_battle',
                         'attracts_gau'])
        self.causes_dark = causes_dark
        self.causes_zombie = causes_zombie
        self.causes_poison = causes_poison
        self.causes_magitek = causes_magitek
        self.causes_vanish = causes_vanish
        self.causes_imp = causes_imp
        self.causes_petrify = causes_petrify
        self.causes_death = causes_death
        self.causes_condemned = causes_condemned
        self.causes_kneeling = causes_kneeling
        self.causes_blink = causes_blink
        self.causes_silence = causes_silence
        self.causes_berserk = causes_berserk
        self.causes_confusion = causes_confusion
        self.causes_hp_drain = causes_hp_drain
        self.causes_sleep = causes_sleep
        self.causes_dance_or_float = causes_dance_or_float
        self.causes_regen = causes_regen
        self.causes_slow = causes_slow
        self.causes_haste = causes_haste
        self.causes_stop = causes_stop
        self.causes_shell = causes_shell
        self.causes_safe = causes_safe
        self.causes_reflect = causes_reflect
        self.causes_rage = causes_rage
        self.causes_frozen = causes_frozen
        self.causes_protection_from_death = causes_protection_from_death
        self.causes_morph = causes_morph
        self.causes_casting = causes_casting
        self.causes_removed = causes_removed
        self.causes_defended_by_interceptor = \
            causes_defended_by_interceptor
        self.causes_float = causes_float
        self.summons_random_esper = summons_random_esper
        self.is_super_ball = is_super_ball
        self.removes_character_from_battle = removes_character_from_battle
        self.is_elixir = is_elixir
        self.removes_all_characters_from_battle = \
            removes_all_characters_from_battle
        self.attracts_gau = attracts_gau

    @classmethod
    def from_rom(cls, rom, number):
        name_offset = cls.NameSize * number
        name_start = rom.ItemNamesOffset+name_offset
        name = _read_dte_string(rom.data, name_start, 13)
        data_offset = cls.DataSize * number
        data_start = rom.ItemDataOffset+data_offset
        type = _read_byte(rom.data, data_start + 0)
        usability = type & 0xF0
        type = type & 0x0F
        targeting = _read_byte(rom.data, data_start + 14)
        item_properties = _read_byte(rom.data, data_start + 19)
        effect_strength = _read_byte(rom.data, data_start + 20)
        caused_conditions1 = _read_byte(rom.data, data_start + 21)
        caused_conditions2 = _read_byte(rom.data, data_start + 22)
        caused_conditions3 = _read_byte(rom.data, data_start + 23)
        caused_conditions4 = _read_byte(rom.data, data_start + 24)
        special_action = _read_byte(rom.data, data_start + 27)
        price = _read_short(rom.data, data_start + 28)
        attributes = {}
        if type != InventoryItemType.Item.value:
            msg = 'Invalid item type in ROM (got %s, expected %s)'
            raise ValueError(msg % (type, InventoryItemType.Item))
        attributes['number'] = number
        attributes['name'] = name
        attributes['type'] = InventoryItemType.Item
        attributes['effect_strength'] = effect_strength
        attributes['price'] = price
        enum_params = [
            ('usability', usability, InventoryItemUsability),
            ('caused conditions 1', caused_conditions1, Condition1, 'causes_'),
            ('caused conditions 2', caused_conditions2, Condition2, 'causes_'),
            ('caused conditions 3', caused_conditions3, Condition3, 'causes_'),
            ('caused conditions 4', caused_conditions4, Condition4, 'causes_'),
            ('targeting', targeting, Targeting, 'targets_'),
        ]
        for args in enum_params:
            attributes.update(get_matching_values_as_params(*args))
        attributes.update(get_matching_values_as_params_limit_one(
            item_properties,
            ItemProperty,
            ignores=[ItemProperty.NoItemProperty.value]))
        attributes.update(get_matching_values_as_params_limit_one(
            special_action,
            SpecialAction,
            ignores=[SpecialAction.NoSpecialAction.value]))
        return cls(**attributes)

class Items:

    def __init__(self, rom, items):
        self._rom = rom
        self._items = items

    @classmethod
    def from_rom(cls, rom):
        items = []
        for n in range(256):
            item_location = rom.ItemDataOffset + (n * InventoryItem.DataSize)
            item_type = _read_byte(rom.data, item_location) & 0x0F
            if item_type == InventoryItemType.Tool.value:
                items.append(Tool.from_rom(rom, n))
            elif item_type == InventoryItemType.Weapon.value:
                items.append(Weapon.from_rom(rom, n))
            elif item_type == InventoryItemType.Armor.value:
                items.append(Armor.from_rom(rom, n))
            elif item_type == InventoryItemType.Shield.value:
                items.append(Shield.from_rom(rom, n))
            elif item_type == InventoryItemType.Hat.value:
                items.append(Hat.from_rom(rom, n))
            elif item_type == InventoryItemType.Relic.value:
                items.append(Relic.from_rom(rom, n))
            elif item_type == InventoryItemType.Item.value:
                items.append(Item.from_rom(rom, n))
            else:
                raise ValueError('Unknown item type in ROM (got %s)' % (type))
        return cls(rom, items)

    def __getitem__(self, item):
        return self._items[item]
