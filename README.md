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
