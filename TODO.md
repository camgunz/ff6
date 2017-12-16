# To Do

- ROM:
  - monsters:
    - sketch
    - control
    - rage
    - steal
    - drop
  - battle dialogue
  - morph packages
  - HP/MP gain
  - character starting equipment
  - character starting stats
  - shops
  - spells
  - bushido
  - blitz
  - Terra/Celes learned magic
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
- ASM hack the item stats loading

## Engineering

- Work on serialization
- Is it even worth having `Struct`, `StructArray` and `VariantStruct` separate
  from `StructField` and `StructArrayField`?  Feels like a lot of indirection
  for nothing because you never use them by themselves.
- Now that things are deserializing, they should be related to the ROM.  So
  instead of Terra's weapon being `1`, it should be `rom.items[1] ('Dirk')`
  - Feels like... `ROMMapper` and `get/set` functions

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
