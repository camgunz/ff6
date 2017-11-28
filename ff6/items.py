class Item:

    Size = 30

    def __init__(self, type, who_equips, relic_effect1, relic_effect2,
                       relic_effect3, status_effect, attack_elements, speed,
                       vigor, magic_power, stamina, abilities_enabled,
                       battle_power, hit_rate, absorb_elements,
                       no_effect_elements, weak_elements, use_effect,
                       magic_block, evade, low_price, high_price):
    self.type = type
    self.who_equips = who_equips
    self.relic_effect1 = relic_effect1
    self.relic_effect2 = relic_effect2
    self.relic_effect3 = relic_effect3
    self.status_effect = status_effect
    self.attack_elements = attack_elements
    self.speed = speed
    self.vigor = vigor
    self.magic_power = magic_power
    self.stamina = stamina
    self.abilities_enabled = abilities_enabled
    self.battle_power = battle_power
    self.hit_rate = hit_rate
    self.absorb_elements = absorb_elements
    self.no_effect_elements = no_effect_elements
    self.weak_elements = weak_elements
    self.use_effect = use_effect
    self.magic_block = magic_block
    self.evade = evade
    self.low_price = low_price
    self.high_price = high_price

class Items:

    Count = 255
    Offset = 185200

    def __init__(self, rom):
        self.rom = rom
        self._cache = [None] * self.Count

    def __iter__(self):
        return (self[x] for x in range(self.ItemCount))

    def __getitem__(self, index):
        item = self._cache[index]
        if item is None:
            self._cache[index] = Item.from_data(
                self.rom.data[self.Offset + (index * Item.Size)]
            )
            item = self._cache[index]
        return item
