from io import StringIO
from enum import Enum

class Character(Enum):
    Terra  = 1 << 0
    Locke  = 1 << 1
    Cyan   = 1 << 2
    Shadow = 1 << 3
    Edgar  = 1 << 4
    Sabin  = 1 << 5
    Celes  = 1 << 6
    Strago = 1 << 7
    Relm   = 1 << 8
    Setzer = 1 << 9
    Mog    = 1 << 10
    Gau    = 1 << 11
    Gogo   = 1 << 12
    Umaro  = 1 << 13
    Imp    = 1 << 14

class InventoryItemType(Enum):
    Tool           = 0
    Weapon         = 1
    Armor          = 2
    Shield         = 3
    Hat            = 4
    Relic          = 5
    Item           = 6

class InventoryItemUsability(Enum):
    Throwable      = 1 << 4
    UsableInBattle = 1 << 5
    UsableInField  = 1 << 6

class Targeting(Enum):
    SingleAllyOrEnemy     = 1 << 0
    AlliesOrEnemiesOnly   = 1 << 1
    AllAlliesAndEnemies   = 1 << 2
    AllAlliesOrAllEnemies = 1 << 3
    OnlyDefaultSelection  = 1 << 4
    Multiple              = 1 << 5
    EnemiesByDefault      = 1 << 6
    Random                = 1 << 7

class ItemProperty(Enum):
    NoItemProperty          = 0
    RestoresHP              = 1 << 3
    RestoresMP              = 1 << 4
    RemovesStatusConditions = 1 << 5
    CausesDamage            = 1 << 6
    EffectIsProportionate   = 1 << 7

class SpecialAction(Enum):
    SummonsRandomEsper             = 1
    isSuperBall                    = 2
    RemovesCharacterFromBattle     = 3
    IsElixir                       = 4
    RemovesAllCharactersFromBattle = 5
    AttractsGau                    = 6
    NoSpecialAction                = 255

class SpecialAttack(Enum):
    NoSpecialAttack                   = 0
    Steals                            = 1
    AttackPowerIncreasesAsHPIncreases = 2
    KillsWithX                        = 3
    DoublesHumanDamage                = 4
    DrainsHP                          = 5
    DrainsMP                          = 6
    AffectsMP                         = 7
    IsDice                            = 9
    AttackPowerIncreasesAsHPDecreases = 10
    HasWindAttack                     = 11
    RecoversHP                        = 12
    Kills                             = 13
    UsesMPForCritical                 = 14
    UsesMoreMPForCritical             = 15

class FieldEffect(Enum):
    ReducesEnemyAttacks  = 1
    PreventsEnemyAttacks = 2
    DoublesWalkingSpeed  = 32
    CuresOneHPPerStep    = 64

class StatusEffect1(Enum):
    RaisesAttackDamage = 1 << 0
    RaisesMagicDamage  = 1 << 1
    RaisesHPOneQuarter = 1 << 2
    RaisesHPOneHalf    = 1 << 3
    RaisesHPOneEighth  = 1 << 4
    RaisesMPOneQuarter = 1 << 5
    RaisesMPOneHalf    = 1 << 6
    RaisesMPOneEighth  = 1 << 7

class StatusEffect2(Enum):
    IncreasesStealRate     = 1 << 0
    EnablesPerfectHitRate  = 1 << 4
    HalvesMPConsumption    = 1 << 5
    SetsMPConsumptionToOne = 1 << 6
    RaisesVigor            = 1 << 7

class Condition1(Enum):
    Dark    = 1 << 0
    Zombie  = 1 << 1
    Poison  = 1 << 2
    Magitek = 1 << 3
    Vanish  = 1 << 4
    Imp     = 1 << 5
    Petrify = 1 << 6
    Death   = 1 << 7

class Condition2(Enum):
    Condemned = 1 << 0
    Kneeling  = 1 << 1
    Blink     = 1 << 2
    Silence   = 1 << 3
    Berserk   = 1 << 4
    Confusion = 1 << 5
    HPDrain   = 1 << 6
    Sleep     = 1 << 7

class Condition3(Enum):
    DanceOrFloat = 1 << 0
    Regen        = 1 << 1
    Slow         = 1 << 2
    Haste        = 1 << 3
    Stop         = 1 << 4
    Shell        = 1 << 5
    Safe         = 1 << 6
    Reflect      = 1 << 7

class Condition4(Enum):
    Rage                  = 1 << 0
    Frozen                = 1 << 1
    ProtectionFromDeath   = 1 << 2
    Morph                 = 1 << 3
    Casting               = 1 << 4
    Removed               = 1 << 5
    DefendedByInterceptor = 1 << 6
    Float                 = 1 << 7

class BattleEffect1(Enum):
    EnablesJump          = 1 << 2
    EnablesXMagic        = 1 << 3
    EnablesControl       = 1 << 4
    EnablesGPRain        = 1 << 5
    EnablesCapture       = 1 << 6
    ForcesContinuousJump = 1 << 7

class BattleEffect2(Enum):
    EnablesXFight          = 1 << 0
    RandomlyCounterAttacks = 1 << 1
    IncreasesEvadeChance   = 1 << 2
    AllowsTwoHands         = 1 << 3
    AllowsDualWield        = 1 << 4
    EnablesHeavyArmor      = 1 << 5
    ProtectsAllies         = 1 << 6

class BattleEffect3(Enum):
    CastsShellOnLowHP   = 1 << 0
    CastsSafeOnLowHP    = 1 << 1
    CastsReflectOnLowHP = 1 << 2
    DoublesExperience   = 1 << 3
    DoublesGold         = 1 << 4
    MakesBodyCold       = 1 << 7

class WeaponProperty(Enum):
    UsableWithBushido     = 1 << 1
    SameDamageFromBackRow = 1 << 5
    UsableWithTwoHands    = 1 << 6
    UsableWithRunic       = 1 << 7

class Element(Enum):
    Fire      = 1 << 0
    Ice       = 1 << 1
    Lightning = 1 << 2
    Poison    = 1 << 3
    Wind      = 1 << 4
    Pearl     = 1 << 5
    Earth     = 1 << 6
    Water     = 1 << 7

def camel_to_snake(s):
    accepted_abbreviations = ('GP', 'HP', 'MP')
    sio = StringIO(s[0].lower())
    skip = False
    for n in range(len(s)):
        if skip:
            skip = False
        elif s[n:n+2] in accepted_abbreviations:
            if n != 0:
                sio.write('_')
            sio.write('%s' % (s[n:n+2].lower()))
            skip = True
        elif n == 0:
            sio.write(s[n].lower())
        elif s[n].islower():
            sio.write(s[n])
        else:
            sio.write('_%s' % (s[n].lower()))
    return sio.getvalue()

def check_data_value(name, value, enum):
    for e in enum:
        if value == e.value:
            return value
    raise ValueError('Invalid %s value %s' % (name, value))

def get_matching_values(name, value, enum, prefix=None, suffix=None):
    prefix = prefix or ''
    suffix = suffix or ''
    return {''.join((prefix, e.name, suffix)):
            (value & e.value != 0) for e in enum}

def get_matching_values_as_params(name, value, enum, prefix=None, suffix=None):
    prefix = prefix or ''
    suffix = suffix or ''
    return {''.join((prefix, camel_to_snake(e.name), suffix)):
            (value & e.value != 0) for e in enum}

def get_matching_values_as_params_limit_one(value, enum, prefix=None,
                                                         suffix=None,
                                                         ignores=None):
    prefix = prefix or ''
    suffix = suffix or ''
    ignores = ignores or []
    params = {camel_to_snake(e.name):
              e.value == value for e in enum if e.value not in ignores}
    if len(list(filter(None, params.values()))) > 1:
        names = [e.name for e in enum if e.value not in ignores]
        msg = 'Only one of %s or %s may be given'
        raise ValueError(msg % (', '.join(names[:-1]), names[-1]))
    return params
