# main.py

from superhero import Superhero, FlyingHero

hero1 = Superhero("Shadow Ninja", "Invisibility")
hero2 = FlyingHero("Sky Eagle", "Wind Blast", 500)

hero1.display_info()
hero1.use_power()

print()

hero2.display_info()
hero2.use_power()
