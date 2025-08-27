# 🐍 OOP in Python – Smartphone & Polymorphism Example

This project demonstrates **Object-Oriented Programming (OOP)** concepts in Python.  
It covers **classes, constructors, inheritance, encapsulation, and polymorphism** with fun examples. 🚀

---

## 📌 Activity 1: Smartphone Class (Encapsulation + Inheritance)

We created a **`Device`** base class and a **`Smartphone`** class that inherits from it.

### Features:
- **Attributes**: brand, model, OS, storage, battery.
- **Methods**:
  - `device_info()` → Returns device brand + model.
  - `install_app(app_name)` → Installs an app.
  - `use_battery(percent)` → Decreases battery level.
  - `charge()` → Recharges the phone.

### Example Usage:
```python
phone1 = Smartphone("Samsung", "S24 Ultra", "Android", "512GB")
phone1.install_app("WhatsApp")
phone1.use_battery(30)
phone1.charge()


ASSIGNMENT 2
# 🚗✈️⛵🚴 Python OOP – Polymorphism with Vehicles

This project demonstrates **Polymorphism** in Python using a `Vehicle` base class and several subclasses (`Car`, `Plane`, `Boat`, `Bicycle`).  
Each subclass overrides the same method `move()`, but implements it differently.

---

## 📌 Code Overview

```python
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
