from io import StringIO
from enum import IntEnum, IntFlag

class ShopType(IntEnum):
    NoType = 0
    Weapon = 1
    Armor = 2
    Item = 3
    Relics = 4
    Vendor = 5

class ShopProperties(IntEnum):
    NormalPrice               = 0
    DoublePrice               = 1
    OneAndAHalfTimesPrice     = 2
    HalfPriceWithEdgarOrSabin = 3

class MagicBall(IntEnum):
    WhiteMagic = 232
    BlackMagic = 233
    GreyMagic = 234

class EsperBonus(IntEnum):
    HPPlus10Percent    = 0x0
    HPPlus30Percent    = 0x1
    HPPlus50Percent    = 0x2
    MPPlus10Percent    = 0x3
    MPPlus30Percent    = 0x4
    MPPlus50Percent    = 0x5
    HPPlus100Percent   = 0x6
    LevelPlus30Percent = 0x7
    LevelPlus50Percent = 0x8
    StrengthPlusOne    = 0x9
    StrengthPlusTwo    = 0xA
    SpeedPlusOne       = 0xB
    SpeedPlusTwo       = 0xC
    StaminaPlusOne     = 0xD
    StaminaPlusTwo     = 0xE
    MagicPowerPlusOne  = 0xF
    MagicPowerPlusTwo  = 0x10
    NoBonus            = 0xFF

class Actor(IntEnum):
    Terra       =  0
    Locke       =  1
    Cyan        =  2
    Shadow      =  3
    Edgar       =  4
    Sabin       =  5
    Celes       =  6
    Strago      =  7
    Relm        =  8
    Setzer      =  9
    Mog         = 10
    Gau         = 11
    Gogo        = 12
    Umaro       = 13
    Banon       = 14
    Leo         = 15
    Ghost1      = 16
    Ghost2      = 17
    Kupek       = 18
    Kupop       = 19
    Kumama      = 20
    Kuku1       = 21
    Kutan       = 22
    Kupan       = 23
    Kushu       = 24
    Kurin       = 25
    Kuku2       = 26
    Kamog       = 27
    FakeMog     = 28
    Unknown1    = 29
    Maduin      = 30
    Unknown2    = 31
    Wedge       = 32
    Vicks       = 33
    Undefined1  = 34
    Undefined2  = 35
    Undefined3  = 36
    Undefined4  = 37
    Undefined5  = 38
    Undefined6  = 39
    Undefined7  = 40
    Kefka1      = 41
    Kefka2      = 42
    Kefka3      = 43
    Kefka4      = 44
    Kefka5      = 45
    Kefka6      = 46
    Kefka7      = 47
    Tork        = 48
    Jade        = 49
    Custer      = 50
    Fabian      = 51
    Drake       = 52
    Sara        = 53
    Case        = 54
    Siele       = 55
    Ray         = 56
    Reiker      = 57
    Lance       = 58
    Bob         = 59
    Pepper      = 60
    Tau         = 61
    Victor      = 62
    Ho          = 63
    Undefined8  = 64
    Undefined9  = 115
    Undefined10 = 255

class Character(IntEnum):
    Terra            =  0
    Locke            =  1
    Cyan             =  2
    Shadow           =  3
    Edgar            =  4
    Sabin            =  5
    Celes            =  6
    Strago           =  7
    Relm             =  8
    Setzer           =  9
    Moogle           = 10
    Gau              = 11
    Gogo             = 12
    Umaro            = 13
    ImperialSoldier1 = 14
    Imp              = 15
    Leo              = 16
    Banon            = 17
    TerraEsper       = 18
    Merchant         = 19
    Ghost            = 20
    Kefka            = 21
    Gesthal          = 22
    Elder            = 23
    ImperialSoldier2 = 24
    Interceptor      = 25
    CelesOpera       = 26
    Scholar          = 27
    Draco            = 28
    Arvis            = 29
    Returner         = 30
    Ultros           = 31
    GauClean         = 32
    Unknown1         = 33
    Counselor        = 34
    Clide            = 35
    OldLady          = 36
    Lady             = 37
    Boy              = 38
    Unknown2         = 39
    Unknown3         = 40
    Unknown4         = 41
    Unknown5         = 42
    Unknown6         = 43
    Unknown7         = 44
    Unknown8         = 45
    Unknown9         = 46
    Unknown10        = 47
    Unknown11        = 48
    Unknown12        = 49
    Unknown13        = 50
    Unknown14        = 51
    Unknown15        = 52
    Unknown16        = 53
    Unknown17        = 212
    Unknown18        = 255

class SaveCharacterStatus(IntFlag):
    Dark      = 1 << 0
    Zombie    = 1 << 1
    Poison    = 1 << 2
    Magitek   = 1 << 3
    Invisible = 1 << 4
    Imp       = 1 << 5
    Stone     = 1 << 6
    Death     = 1 << 7
    Unknown1  = 1 << 8
    Unknown2  = 1 << 9
    Unknown3  = 1 << 10
    Unknown4  = 1 << 11
    Unknown5  = 1 << 12
    Unknown6  = 1 << 13
    Unknown7  = 1 << 14
    Float     = 1 << 15

class BattleCommand(IntEnum):
    Fight   = 0
    Item    = 1
    Magic   = 2
    Empty1  = 3
    Morph   = 4
    Steal   = 5
    Capture = 6
    Bushido = 7
    Throw   = 8
    Tools   = 9
    Blitz   = 10
    Runic   = 11
    Lore    = 12
    Sketch  = 13
    Control = 14
    Slot    = 15
    Rage    = 16
    Leap    = 17
    Mimic   = 18
    Dance   = 19
    Row     = 20
    Def     = 21
    Jump    = 22
    XMagic  = 23
    GPRain  = 24
    Summon  = 25
    Health  = 26
    Shock   = 27
    Possess = 28
    Magitek = 29
    Empty2  = 255

class MagicExtraEffect(IntEnum):
    Nothing1                                          = 0
    Steal                                             = 1
    KillRandomly                                      = 3
    UseRandomGraphic                                  = 9
    ShowEnemyStats                                    = 16
    CreateEarthWall                                   = 17
    MorphTarget                                       = 18
    JumpCaster                                        = 19
    DistributeCasterHPAndMP                           = 21
    RemoveCasterAndCureAllies                         = 22
    Tapir                                             = 23
    WarpOutOfBattle                                   = 24
    SacrificeCasterForHPDamage                        = 25
    DoOneThousandDamage                               = 26
    BaseEffectOnCasterHP                              = 27
    AffectOnlyReflectedTargets                        = 28
    AffectOnlyTargetsWhereLastGPDigitIsLevelFactor    = 29
    BaseEffectOnSteps                                 = 30
    HalveTargetLevel                                  = 31
    SacrificeCasterForAllyCure                        = 32
    ExchangeStatusEffects                             = 33
    IncreaseDamageIfTargetLevelEqualsCasterLevel      = 34
    CancelEnemyDesperationAttack                      = 35
    Crusader                                          = 36
    CannotAffectFloatingTargets                       = 37
    ChangeAbsorbedElement                             = 38
    RunAway                                           = 39
    MindBlast                                         = 40
    FreezeTarget                                      = 41
    MultiplyEffectByLowestAllyLevel                   = 42
    SwitchTargetRow                                   = 43
    CastEightTimes                                    = 44
    MakeTargetInterceptPhysicalAttacksTargetingCaster = 45
    SeizeTargetAndDrainHP                             = 46
    Targeting                                         = 47
    HalveDamageIfMultipleEnemiesRemain                = 48
    NullifyRandomElement                              = 49
    CastFourTimes                                     = 50
    Bababreath                                        = 51
    CharmTarget                                       = 52
    Doom                                              = 53
    Empowerer                                         = 54
    ZombieCountdown                                   = 55
    RemoveTargetFromBattle                            = 56
    RemoveTargetFromBattleAndWarpToTriangleIsland     = 57
    PossessTarget                                     = 58
    ActivateRandomStatus                              = 59
    Retort                                            = 60
    BaseEffectOnMissingHP                             = 61
    UncurableHPDrain                                  = 62
    Stunner                                           = 63
    DropHPToOne                                       = 64
    GiveTargetTwoTurns                                = 67
    ReturnTarget                                      = 68
    Clear                                             = 69
    SuperBall                                         = 74
    KillCasterAndTarget                               = 80
    StealTargetGP                                     = 82
    Control                                           = 83
    Leap                                              = 84
    GiveTargetRandomWeakness                          = 86
    TargetDiesIfItActs                                = 87
    Nothing2                                          = 255

class MagicProperty(IntFlag):
    CausesPhysicalDamage             = 1 << 0
    MissesIfTargetProtectedFromDeath = 1 << 1
    TargetsOnlyDeadAllies            = 1 << 2
    InvertsDamageOnUndead            = 1 << 3
    TargetIsRandomized               = 1 << 4
    IgnoresTargetDefense             = 1 << 5
    FullDamageWithMultipleTargets    = 1 << 6
    AbortIfAllyTargeted              = 1 << 7
    UsableOutsideBattle              = 1 << 8
    NotReflectable                   = 1 << 9
    LearnableAsLore                  = 1 << 10
    VulnerableToRunic                = 1 << 11
    WarpOrQuick                      = 1 << 12
    RetargetsIfTargetInvalid         = 1 << 13
    KillsCaster                      = 1 << 14
    AffectsMP                        = 1 << 15
    Heals                            = 1 << 16
    Redirects                        = 1 << 17
    LiftsStatus                      = 1 << 18
    TogglesStatus                    = 1 << 19
    BasesDefenseOnStamina            = 1 << 20
    CannotBeDodged                   = 1 << 21
    HitCountBasedOnHitRate           = 1 << 22
    ProportionalDamage               = 1 << 23

class MagicPropertyExtra(IntFlag):
    MissesIfTargetProtectedFromAilments = 1 << 0
    DisplaysMessageOnHit                = 1 << 1

class EquipInfo(IntFlag):
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
    Heavy  = 1 << 15

class InventoryItemType(IntEnum):
    Tool           = 0
    Weapon         = 1
    Armor          = 2
    Shield         = 3
    Hat            = 4
    Relic          = 5
    Item           = 6

class EquipmentIconType(IntEnum):
    Knife    = 0xD8
    Sword    = 0xD9
    Spear    = 0xDA
    Katana   = 0xDB
    Rod      = 0xDC
    Brush    = 0xDD
    Shuriken = 0xDE
    Special  = 0xDF
    Gambler  = 0xE0
    Claw     = 0xE1
    Shield   = 0xE2
    Hat      = 0xE3
    Armor    = 0xE4
    Tool     = 0xE5
    Skean    = 0xE6
    Relic    = 0xE7
    NoIcon   = 0xFF

class InventoryItemUsability(IntFlag):
    Throwable      = 1 << 0
    UsableInBattle = 1 << 1
    UsableInField  = 1 << 2

class Targeting(IntFlag):
    SingleAllyOrEnemy     = 1 << 0
    AlliesOrEnemiesOnly   = 1 << 1
    AllAlliesAndEnemies   = 1 << 2
    AllAlliesOrAllEnemies = 1 << 3
    OnlyDefaultSelection  = 1 << 4
    Multiple              = 1 << 5
    EnemiesByDefault      = 1 << 6
    Random                = 1 << 7

class ItemProperty(IntFlag):
    NoItemProperty          = 0
    ReverseDamageOnUndead   = 1 << 1
    RestoresHP              = 1 << 3
    RestoresMP              = 1 << 4
    RemovesStatusConditions = 1 << 5
    CausesDamage            = 1 << 6
    EffectIsProportionate   = 1 << 7

class ItemSpecialAction(IntEnum):
    NoSpecialAction1               = 0
    SummonsRandomEsper             = 1
    IsSuperBall                    = 2
    RemovesCharacterFromBattle     = 3
    IsElixir                       = 4
    WarpsCharactersFromBattle      = 5
    AttractsGau                    = 6
    NoSpecialAction2               = 255

class WeaponSpecialAttack(IntEnum):
    NoSpecialAttack                   = 0
    Steals                            = 1
    AttackPowerIncreasesAsHPIncreases = 2
    KillsWithX                        = 3
    DoublesHumanDamage                = 4
    DrainsHP                          = 5
    DrainsMP                          = 6
    UsesMPForCritical                 = 7
    RandomlyThrows                    = 8
    IsDice                            = 9
    AttackPowerIncreasesAsHPDecreases = 10
    HasWindAttack                     = 11
    RecoversHP                        = 12
    Kills                             = 13
    RandomlyBreaks                    = 14

class EvadeAnimation(IntEnum):
    Nothing1                  = 0
    Nothing2                  = 1
    Nothing3                  = 2
    Nothing4                  = 3
    Knife1                    = 4
    Sword1                    = 5
    BucklerPhysical           = 6
    RedCape1                  = 7
    Nothing5                  = 8
    Nothing6                  = 9
    BucklerMagical            = 10
    Nothing7                  = 11
    Knife2                    = 12
    Sword2                    = 13
    BucklerPhysicalAndMagical = 14
    RedCape2                  = 15

class FieldEffect(IntFlag):
    ReducesEnemyAttacks  = 1 << 0
    PreventsEnemyAttacks = 1 << 1
    DoublesWalkingSpeed  = 1 << 5
    CuresOneHPPerStep    = 1 << 7

class StatusEffect1(IntFlag):
    RaisesAttackDamage = 1 << 0
    RaisesMagicDamage  = 1 << 1
    RaisesHPOneQuarter = 1 << 2
    RaisesHPOneHalf    = 1 << 3
    RaisesHPOneEighth  = 1 << 4
    RaisesMPOneQuarter = 1 << 5
    RaisesMPOneHalf    = 1 << 6
    RaisesMPOneEighth  = 1 << 7

class StatusEffect2(IntFlag):
    IncreasesStealRate     = 1 << 0
    IncreasesSketchRate    = 1 << 2
    IncreasesControlRate   = 1 << 3
    EnablesPerfectHitRate  = 1 << 4
    HalvesMPConsumption    = 1 << 5
    SetsMPConsumptionToOne = 1 << 6
    RaisesVigor            = 1 << 7

class MonsterConditionImmunity(IntFlag):
    DanceOrFloat = 1 << 0
    Regen        = 1 << 1
    Slow         = 1 << 2
    Haste        = 1 << 3
    Stop         = 1 << 4
    Shell        = 1 << 5
    Safe         = 1 << 6
    Reflect      = 1 << 7
    Condemned    = 1 << 8
    Kneeling     = 1 << 9
    Blink        = 1 << 10
    Silence      = 1 << 11
    Berserk      = 1 << 12
    Confusion    = 1 << 13
    HPDrain      = 1 << 14
    Sleep        = 1 << 15
    Dark         = 1 << 16
    Zombie       = 1 << 17
    Poison       = 1 << 18
    Magitek      = 1 << 19
    Vanish       = 1 << 20
    Imp          = 1 << 21
    Petrify      = 1 << 22
    Death        = 1 << 23

class Condition1(IntFlag):
    Dark    = 1 << 0
    Zombie  = 1 << 1
    Poison  = 1 << 2
    Magitek = 1 << 3
    Vanish  = 1 << 4
    Imp     = 1 << 5
    Petrify = 1 << 6
    Death   = 1 << 7

class Condition2(IntFlag):
    Condemned = 1 << 0
    Kneeling  = 1 << 1
    Blink     = 1 << 2
    Silence   = 1 << 3
    Berserk   = 1 << 4
    Confusion = 1 << 5
    HPDrain   = 1 << 6
    Sleep     = 1 << 7

class Condition3(IntFlag):
    DanceOrFloat = 1 << 0
    Regen        = 1 << 1
    Slow         = 1 << 2
    Haste        = 1 << 3
    Stop         = 1 << 4
    Shell        = 1 << 5
    Safe         = 1 << 6
    Reflect      = 1 << 7

class Condition4(IntFlag):
    Rage                  = 1 << 0
    Frozen                = 1 << 1
    ProtectionFromDeath   = 1 << 2
    Morph                 = 1 << 3
    Casting               = 1 << 4
    Removed               = 1 << 5
    DefendedByInterceptor = 1 << 6
    Float                 = 1 << 7

class Condition(IntFlag):
    Dark                  = 1 << 0
    Zombie                = 1 << 1
    Poison                = 1 << 2
    Magitek               = 1 << 3
    Vanish                = 1 << 4
    Imp                   = 1 << 5
    Petrify               = 1 << 6
    Death                 = 1 << 7
    Condemned             = 1 << 8
    Kneeling              = 1 << 9
    Blink                 = 1 << 10
    Silence               = 1 << 11
    Berserk               = 1 << 12
    Confusion             = 1 << 13
    HPDrain               = 1 << 14
    Sleep                 = 1 << 15
    DanceOrFloat          = 1 << 16
    Regen                 = 1 << 17
    Slow                  = 1 << 18
    Haste                 = 1 << 19
    Stop                  = 1 << 20
    Shell                 = 1 << 21
    Safe                  = 1 << 22
    Reflect               = 1 << 23
    Rage                  = 1 << 24
    Frozen                = 1 << 25
    ProtectionFromDeath   = 1 << 26
    Morph                 = 1 << 27
    Casting               = 1 << 28
    Removed               = 1 << 29
    DefendedByInterceptor = 1 << 30
    Float                 = 1 << 31

class BattleEffect1(IntFlag):
    IncreasesPreemptiveAttackRate = 1 << 0
    AllowsRunningInSideAttack     = 1 << 1
    EnablesJump                   = 1 << 2
    EnablesXMagic                 = 1 << 3
    EnablesControl                = 1 << 4
    EnablesGPRain                 = 1 << 5
    EnablesCapture                = 1 << 6
    ForcesContinuousJump          = 1 << 7

class BattleEffect2(IntFlag):
    EnablesXFight          = 1 << 0
    RandomlyCounterAttacks = 1 << 1
    IncreasesEvadeChance   = 1 << 2
    AllowsTwoHands         = 1 << 3
    AllowsDualWield        = 1 << 4
    EnablesHeavyArmor      = 1 << 5
    ProtectsAllies         = 1 << 6

class BattleEffect3(IntFlag):
    CastsShellOnLowHP   = 1 << 0
    CastsSafeOnLowHP    = 1 << 1
    CastsReflectOnLowHP = 1 << 2
    DoublesExperience   = 1 << 3
    DoublesGold         = 1 << 4
    MakesBodyCold       = 1 << 7

class WeaponProperty(IntFlag):
    UsableWithBushido     = 1 << 1
    SameDamageFromBackRow = 1 << 5
    UsableWithTwoHands    = 1 << 6
    UsableWithRunic       = 1 << 7

class Element(IntFlag):
    Fire      = 1 << 0
    Ice       = 1 << 1
    Lightning = 1 << 2
    Poison    = 1 << 3
    Wind      = 1 << 4
    Pearl     = 1 << 5
    Earth     = 1 << 6
    Water     = 1 << 7

class MetamorphChance(IntEnum):
    Always = 0
    ThreeQuarters = 1
    Half = 2
    Quarter = 3
    Eighth = 4
    Sixteenth = 5
    ThirtySecond = 6
    NoChance = 7

class MonsterFlag1(IntFlag):
    DiesIfMPExhausted = 1 << 0
    NameHidden        = 1 << 2
    Human             = 1 << 4
    WeakAgainstImps   = 1 << 6
    Undead            = 1 << 7

class MonsterFlag2(IntFlag):
    HarderToRunFrom   = 1 << 0
    AttacksFirst      = 1 << 1
    BlocksSuplex      = 1 << 2
    BlocksRun         = 1 << 3
    BlocksScan        = 1 << 4
    BlocksSketch      = 1 << 5
    SpecialEvent      = 1 << 6
    BlocksControl     = 1 << 7

class MonsterFlag3(IntFlag):
    CoversAllies      = 1 << 0
    UsesRunic         = 1 << 1
    StartsWithLife3   = 1 << 2
    StartsWithFloat   = 1 << 7

class MonsterAttackType(IntEnum):
    MultipleSpikedStars                     = 0
    WhiteDiagonalSlash                      = 1
    ThinWhiteDiagonalSlash                  = 2
    UpsideDownRedWhiplash                   = 3
    WhiteWhipLash                           = 4
    ThickSkyBlueWhipLash                    = 5
    ThickHorizontalWhiteSlash               = 6
    WhiteCrescentSlash                      = 7
    RedClawSlash                            = 8
    GreenBiteMarks                          = 9
    TripleHorizontalWhiteSlashes            = 10
    HorizontalWhiteSlash                    = 11
    WhiteExpandingStar                      = 12
    WhiteTopToBottomSlash                   = 13
    WhiteBiteMarks                          = 14
    Needles                                 = 15
    BlackCircularExplosion                  = 16
    HeadHammer                              = 17
    FlyingBone                              = 18
    FlyingWrench                            = 19
    WhiteLightningBolt                      = 20
    BlueWhiteBeamsOfLight                   = 21
    RobotHand                               = 22
    PuddleOfGoo                             = 23
    BlueBubbles                             = 24
    FlyingMusicNote                         = 25
    FlyingHeart                             = 26
    Wheel                                   = 27
    BloomingFlowers                         = 28
    FlyingMissile                           = 29
    Net                                     = 30
    FlyingDrill                             = 31
    FallingBlackBall                        = 32
    GreySkullSlash                          = 33
    ThickDiagonalWhiteSlashBlackMagicSound1 = 34
    ThickDiagonalWhiteSlashBlackMagicSound2 = 35
    DiagonalWhiteSlashWhiteMagicSound       = 36
    ThickDiagonalWhiteSlashBlackMagicSound3 = 37
    ThickDiagonalWhiteSlashBlackMagicSound4 = 38
    WhiteWhipLashBlackMagicSound            = 39
    WhiteWhipLashRunningAwaySound1          = 40
    DiagonalWhiteSlashBlackMagicSound       = 41
    UpsideDownWhiteWhipLashBlackMagicSound  = 42
    BlackWhipLashRunningAwaySound           = 43
    WhiteAndGreyDiagonalSlash1              = 44
    WhiteAndGreyDiagonalSlash2              = 45
    WhiteAndGreyDiagonalSlash3              = 46
    WhiteAndGreyDiagonalSlash4              = 47
    UpsideDownWhiteWhipLashWhiteMagicIntro  = 48
    WhiteAndGreyDiagonalSlash5              = 49
    WhiteAndGreyDiagonalSlash6              = 50
    WhiteWhipLashRunningAwaySound2          = 51
    ReverseWhiteAndGreyDiagonalSlash        = 52
    WhiteAndGreyDiagonalSlash7              = 53
    WhiteAndGreyDiagonalSlash8              = 54
    WhiteAndGreyDiagonalSlash9              = 55
    WhiteOutlineWhipLashRunningAwaySound    = 63
    TurnAllCharactersToStone                = 68
    GlitchyFallenOne                        = 88
    GlitchySilence                          = 255

class MonsterSpecialAttackEffect(IntEnum):
    Blind                 = 0
    Zombie                = 1
    Poison                = 2
    Clear                 = 4
    Imp                   = 5
    Stone                 = 6
    Death                 = 7
    Count                 = 8
    NearDeath             = 9
    Image                 = 10
    Mute                  = 11
    Berserk               = 12
    Confused              = 13
    HPDrain               = 14
    Sleep                 = 15
    Dance                 = 16
    Regen                 = 17
    Slow                  = 18
    Haste                 = 19
    Stop                  = 20
    Shell                 = 21
    Safe                  = 22
    Wall                  = 23
    Rage                  = 24
    Freeze                = 25
    Life3                 = 26
    Morph                 = 27
    Chant                 = 28
    DisappearAndBerserk   = 29
    DogBlock              = 30
    Float                 = 31
    PhysicalLevelOne      = 32
    PhysicalLevelTwo      = 33
    PhysicalLevelThree    = 34
    PhysicalLevelFour     = 35
    PhysicalLevelFive     = 36
    PhysicalLevelSix      = 37
    PhysicalLevelSeven    = 38
    PhysicalLevelEight    = 39
    PhysicalLevelNine     = 40
    PhysicalLevelTen      = 41
    PhysicalLevelEleven   = 42
    PhysicalLevelTwelve   = 43
    PhysicalLevelThirteen = 44
    PhysicalLevelFourteen = 45
    PhysicalLevelFifteen  = 46
    PhysicalLevelSixteen  = 47
    Drain                 = 48
    Osmose                = 49
    RemoveReflect1        = 50
    RemoveReflect2        = 51
    RemoveReflect3        = 52
    RemoveReflect4        = 53
    RemoveReflect5        = 54
    RemoveReflect6        = 55
    RemoveReflect7        = 56
    RemoveReflect8        = 57
    RemoveReflect9        = 58
    RemoveReflect10       = 59
    RemoveReflect11       = 60
    RemoveReflect12       = 61
    RemoveReflect13       = 62
    RemoveReflect14       = 63
