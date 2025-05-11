# move_test.py

from vehicle import Vehicle, Car, Plane, Boat

vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
