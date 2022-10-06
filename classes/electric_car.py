"""Module created for electric car"""

from car import Car

class ElectricCar(Car):
    """Initialize attributes of  the parent class"""
    def __init__(self, make, model, year, odmeter_reading):
        super().__init__(make, model, year, odmeter_reading)
        self.battery_size = 75

    def battery_info(self):
        print(f"This car has a battery size of {self.battery_size} KWH")

    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100
            print(f"battry size changed to {self.battery_size} KWH")
        elif self.battery_size == 100:
            self.battery_size += 100
            print(f"battry size incremented to {self.battery_size} KWH")
        else:
            self.battery_size
            print(f"battry size is alredy upto date {self.battery_size} KWH")