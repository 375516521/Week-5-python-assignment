# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"

# Child class (Inheritance from Device)
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)  # Inherit brand & model
        self.os = os
        self.storage = storage
        self.battery = 100  # Default battery percentage

    def install_app(self, app_name):
        print(f"Installing {app_name} on {self.device_info()}...")

    def use_battery(self, percent):
        if percent > self.battery:
            print("Battery too low! Please charge 🔋")
        else:
            self.battery -= percent
            print(f"Used {percent}%. Battery left: {self.battery}%")

    def charge(self):
        self.battery = 100
        print(f"{self.device_info()} is now fully charged! ⚡")


# Example usage
phone1 = Smartphone("Samsung", "S24 Ultra", "Android", "512GB")
phone1.install_app("WhatsApp")
phone1.use_battery(30)
phone1.charge()
