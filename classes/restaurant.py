class Restaurant:
    """Class for all restaurant instances"""

    def __init__(self,restaurant_name, cuisine_type, number_served):
        """Initilize attributes for a Restaurant class"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    
    def describe_restaurant(self):
        """Print restaurant name and type"""
        print(f"{self.restaurant_name} is an {self.cuisine_type} restaurant")

    def open_restaurant(self):
        """Print restaurant is OPEN"""
        print(f"{self.restaurant_name} is NOW OPEN !!!")

    def set_number_served(self, number):
        """Method to set the value of number served"""
        if number >= self.number_served:
            self.number_served = number 
            print(f"Served Number has gone up to {number}")
        else:
            print(f"Served Number can only increase")

    def increment_number_served(self):
        """Method to increment the value of number served"""
        self.number_served += 1
        print(f"Served Number was incremented {self.number_served}") 

class IceCreamStand(Restaurant):
    """Class for all icc cream instances"""
    
    """Initialize attributes of  the parent class"""
    def __init__(self, restaurant_name, cuisine_type, number_served):
        super().__init__(restaurant_name, cuisine_type, number_served)

    def ice_cream(self, flavors):
        """Print all the flavors"""
        self.flavors = flavors
        print(f"This Ice Cream Stand has the following flavors: {self.flavors}")