# superhero.py

class Superhero:
    def __init__(self, name, power):
        self.name = name
        self._power = power  # underscore means it's intended to be 'protected'

    def display_info(self):
        print(f"🦸 Name: {self.name}")
        print(f"🧠 Power: {self._power}")

    def use_power(self):
        print(f"{self.name} uses {self._power}!")

# Inherited class
class FlyingHero(Superhero):
    def __init__(self, name, power, flight_speed):
        super().__init__(name, power)
        self.flight_speed = flight_speed

    def use_power(self):  # polymorphism through method overriding
        print(f"{self.name} flies at {self.flight_speed} km/h with {self._power}!")
