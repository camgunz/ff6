#!/usr/bin/env python

import pprint

from ff6.data import *
from ff6.ff6rom import FF6ROM

ROM_FILENAME = 'ff6.rom'

def get_rom(rom_filename):
    rom = FF6ROM.from_file(rom_filename)
    rom.deserialize()
    return rom

def test_monsters(rom_filename):
    rom = get_rom(rom_filename)
    for n, monster in enumerate(rom.monsters):
        print(n, pprint.pformat(monster))

def print_condition2(rom):
    print('name         , condemned, kneeling, blink, silence, berserk, confusion, hp_drain, sleep')
    for item in rom.items:
        if item.type not in (InventoryItemType.Armor, InventoryItemType.Shield,
                             InventoryItemType.Hat, InventoryItemType.Relic):
            continue
        print('%13s: %9s, %8s, %5s, %7s, %7s, %9s, %8s, %5s' % (
            item.name,
            str(item.causes_condemned),
            str(item.causes_kneeling),
            str(item.causes_blink),
            str(item.causes_silence),
            str(item.causes_berserk),
            str(item.causes_confusion),
            str(item.causes_hp_drain),
            str(item.causes_sleep)
        ))

def print_attack_when_used(rom):
    for item in rom.items:
        if item.type == InventoryItemType.Item:
            continue
        print('%13s: %s' % (item.name, item.attack_when_used))

def print_targeting(rom):
    print('         name, single, allies/enemies, everyone, all allies/enemies, only default, multiple, default enemy, random')
    for item in rom.items:
        print('%13s: %6s, %14s, %8s, %18s, %12s, %8s, %13s, %6s' % (
            item.name,
            item.targets_single_ally_or_enemy,
            item.targets_allies_or_enemies_only,
            item.targets_all_allies_and_enemies,
            item.targets_all_allies_or_all_enemies,
            item.targets_only_default_selection,
            item.targets_multiple,
            item.targets_enemies_by_default,
            item.targets_random
        ))

def main():
    test_monsters(ROM_FILENAME)

main()
