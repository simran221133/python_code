"""Module created for car"""

class Car:
    """Class for all car instances"""
    def __init__(self, make, model, year, odmeter_reading):
        """Initilize attributes for a Car Class"""
        self.make = make
        self.model = model
        self.year = year
        self.odmeter_reading = odmeter_reading

    def get_descriptive_name(self):
        """Print car information"""
        info = f"{self.make} {self.model} {self.year}"
        print(info.title())

    def update_odmeter(self, milage):
        if milage > self.odmeter_reading:
            self.odmeter_reading = milage
            print(f"The car has {self.odmeter_reading} kms")
        else:
            print(f"The mileage cannot be decreased from {self.odmeter_reading} to {milage}")
