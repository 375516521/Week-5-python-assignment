
class Vehicle:
    def move(self):
        pass  # Placeholder (to be overridden by subclasses)

class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road...")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky...")

class Boat(Vehicle):
    def move(self):
        print("⛵ Sailing on water...")

class Bicycle(Vehicle):
    def move(self):
        print("🚴 Pedaling on the path...")

# Demonstrating polymorphism
vehicles = [Car(), Plane(), Boat(), Bicycle()]

for v in vehicles:
    v.move()  # Same method name, but different behavior!
