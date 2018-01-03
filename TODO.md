# To Do

## Data

- ROM:
  - Battle dialogue
  - Esper Descriptions (0x0F3B40, variable strings)
  - Blitz Specifications (0x035E1C, 14 elements, 2 bytes: char, rotation)
  - Checksum

- Save game:
  - Magic
  - Bushido
  - Blitz
  - Lores
  - Espers
  - Rages
  - Current party
  - Checksum

## To Find

- Magitek menu configuration

## Maybe

Monster AI.  I feel like this could be pretty simple, actually.

## Hacking

- Esper Stat Gains:
  - Basically make the stat gains bigger
- Item stats:
  - Change the data format for items
  - ASM hack the item stats loading

## Engineering

- Save games need a ROM to reference, which complicates the field structure a
  little

## Discussed

### Magic

Only some characters will be able to learn all the magic.

It's likely that even very not-magical characters will be able to learn some
specific spells, like Locke might learn Quick.

Some characters will be able to learn all the magic:
- Terra
- Strago
- Relm

I'm not really sure if that's necessary though.  Relm's ability is only bad
because it's setup badly, and we can fix that.  Strago's ability is also fine.
I think it might make sense for there to be spells that definitly only Terra,
and maybe only Celes, know.

We'll gate magic with equipment.

### Celes

We discussed pushing Celes more into the physical realm, but came to no real
conclusion.  I think if we do that then we nerf the spells she learns/is able
to learn.

### Relm

Make her Sketch/Control possibilities better.

### Shadow

Make him a lot easier to kill.

### Setzer

Hard to say, no real conclusions.

### Locke

Get rid of Thief Glove.  Either you get a good hit or you steal; Capture lets
you turn your brain off and that's not the goal.

Consider making steal always work, or at least close to always work.

### Edgar

NoiseBlaster should be 1 enemy only.

### Equipment

Characters won't be able to equip anything they want.  This is mostly to gate
magic but also to make sense (Relm can't use a huge spear, only Relm can paint
with Brushes, etc.)

### Espers

Espers don't grant magic, or if they do it's pretty weak.

We want to enhance the stat boosts to justify getting really strong via the use
of Espers.  Therefore espers won't have _bad_ stat boosts.

### Items

Get rid of all curative items except for Dried Meat.  Also get rid of Remedy.
Probably drop Tincture down to affordability.

Get rid of superfluous items like:
- Gauntlet
- Genji Glove
- Rename Card
- Etc.

## To Consider

### Steal x4 patch

Just feels better honestly: more variety.

### Really low HP gains

It doesn't really make sense for humans to start out at 300hp, but after
fighting 10,000 rabbits, they can withstand a meteor shower.

You could do this in a number of ways, but because thousands feels a lot cooler
than hundreds, maybe we want to start close to 1k but top out around 2k or 2.5k.

The level curve ends up that you get to 23-27 around the floating continent,
which I think is cool. So if your range is 800-2800 the diff is 2000 and that
means 20hp per level which means you should be 1,200 by floating continent.

Let's bump that down to 500-2500, so 25 levels of 20 HP is 500HP, so yeah
you'll be around exactly 1,000.

### Stealing pelts/hides/etc. from animals

I struggle to really think of what you could meaningfully steal from animals.
You can get away with some conceits: the hounds in Narshe maybe having some
reviving tonics or un-freezing juice (whatever), but what does a Rabite have?
Are you gonna steal lettuce?  Can you justify like, yoinking a tooth or a foot
with only steal instead of capture -- shouldn't that cause damage?

I'm drawn to the idea that stealing is kind of like an abbreviated fur shop
mechanic.  Like you steal from a Poison Dragon and get a Poison Claw.

So maybe that is the mechanic.  Either you get a pelt or something, or you fur
shop them into equipment and usable items.

But that raises the question about drops.  Under that logic, shouldn't drops be
exactly the same?  What separates 'steal' from 'drop' in the context of FF6.
Normally you'd think, "well I stole your sword so you can't hit me", which is
the FFT way of doing things, but FF6 is essentially just "extra, cool items".

I think applying "realism logic" to this just ruins the mechanic like BNW does.
The only conclusion that works within the confines of FF6's code is, "stealing
from animals shouldn't really be useful", which wastes the mechanic and really
nerfs Locke's ability.

So therefore I think steal should be "like drops but cooler", and at least
marginally related to the monster itself.  Plus it's fundamentally "now I have
two of these things", and double drops is a strong economic incentive.

Re: Pelts, I think animals don't drop gold but they do drop pelts.  That feels
like an easy improvement.

### Removing tents and most healing items

Most of this stuff is easy mode.  I do like the idea of special buffing items
like Hero Drink from DM or Red Bull (not actual Red Bull though) from BNW.

Elixir
Megalixir
Dried Meat

Grade A Pelt
Grade B Pelt
Grade C Pelt
Grade D Pelt
Grade E Pelt

Grade X Pelt

Grade S Pelt

Magical Pelt
Leather Pelt
Armored Pelt
Cursed Pelt
Holy Pelt
Mystery Pelt

Grade AA Pelt

Tonic
Potion
X-Potion
Tincture
Ether
X-Ether
Sleeping Bag
Tent

### Offensive items

I also really want an offensive item like Grenade or Molotov, but dunno if that
can really be done or is worth it... also isn't that Shuriken?

Does it make sense for there to be low level "throwables" that everyone can
"use"?  Or they might not necessarily be low level but maybe we buff the stars
to hit all enemies?

Nah I think leave this one alone.  This is Shadow's domain.

I used to wish effects still worked via Throw, but I think that's probably OP.
You shouldn't be able to deal a lot of damage OR effects from the back row
regardless of equipment.  So this probably works out.
