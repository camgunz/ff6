from enum import Enum, IntEnum

class EquipCharacter(IntEnum):
    Terra = 1 << 0
    Locke = 1 << 1
    Cyan = 1 << 2
    Shadow = 1 << 3
    Edgar = 1 << 4
    Sabin = 1 << 5
    Celes = 1 << 6
    Strago = 1 << 7
    Relm = 1 << 8
    Setzer = 1 << 9
    Mog = 1 << 10
    Gau = 1 << 11
    Gogo = 1 << 12
    Umaro = 1 << 13
    Imp = 1 << 14

    @classmethod
    def equipping_characters(cls, value):
        return [char for char in cls if value & char != 0]

class WeaponAbilities(IntEnum):
    Bushido = 1 << 1
    TwoHand = 1 << 5
    Runic = 1 << 6

    @classmethod
    def enabled_abilities(cls, value):
        return [ability for ability in cls if value & ability != 0]

class MagicBlockAndEvadeValues(IntEnum):
    Ten = 1
    Twenty = 2
    Thirty = 3
    Forty = 4
    Fifty = 5
    NegativeTen = 6
    NegativeTwenty = 7
    NegativeThirty = 8
    NegativeForty = 9
    NegativeFifty = 10
    Zero = 11
    Max1 = 12
    Max2 = 13
    Max3 = 14
    Max4 = 15

    def is_max(self):
        return isinstance(self, (self.Max1, self.Max2, self.Max3, self.Max4))

class StatBonusValues(IntEnum):
    Zero = 0
    One = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 0
    NegativeOne = -1
    NegativeTwo = -2
    NegativeThree = -3
    NegativeFour = -4
    NegativeFive = -5
    NegativeSix = -6
    NegativeSeven = -7

class MagicDamageFlag(IntEnum):
    DoesDamage = 1 << 1
    MPInsteadOfHP = 1 << 3

class MagicUsableOutsideBattle(IntEnum):
    Yes = 1 << 0
    No = 1 << 1

class MagicEffect(IntEnum):
    HealHP = 1 << 0
    AbsorbHP = 1 << 1
    RemoveStatus = 1 << 2
    GiveStatus = 1 << 3
    NeverMisses = 1 << 5
    FractionalDamage = 1 << 7

class MagicSpecialEffect(IntEnum):
    Pummel = 0x00
    Scan = 0x10
    Golem = 0x11
    Ragnarok = 0x12
    Palidor = 0x13
    mantra = 0x15
    Spiraler = 0x16
    Warp = 0x18

