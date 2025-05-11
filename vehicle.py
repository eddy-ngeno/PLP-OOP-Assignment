# vehicle.py

class Vehicle:
    def move(self):
        print("Generic vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("🚗 Car is driving.")

class Plane(Vehicle):
    def move(self):
        print("✈️ Plane is flying.")

class Boat(Vehicle):
    def move(self):
        print("⛵ Boat is sailing.")
