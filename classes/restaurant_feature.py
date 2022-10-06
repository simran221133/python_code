from restaurant import Restaurant
from restaurant import IceCreamStand

"""Creating instance one(ice_cream1) of class IceCreamStand"""
ice_cream1 = IceCreamStand("Baskin Robin", "English", 15)
ice_cream1.ice_cream(['Mango', 'Strawberry', 'Chocolate', 'Very Berry'])

"""Creating instance one(restaurant) of class Restaurant"""
restaurant = Restaurant("Bombay Bhel", "Indian", 20)
restaurant.number_served = 25
restaurant.set_number_served(10)
print(f"Restaurant Name: {restaurant.restaurant_name}")
print(f"Cuisine Name: {restaurant.cuisine_type}")
print(f"Number of Customers: {restaurant.number_served}")
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.increment_number_served()
print("")

"""Creating instance two(r_2) of class Restaurant"""
r_2 = Restaurant("Mel Dinner", "English", 11)
r_2.number_served = 20
r_2.set_number_served(33)
print(f"Restaurant Name: {r_2.restaurant_name}")
print(f"Cuisine Name: {r_2.cuisine_type}")
print(f"Number of Customers: {r_2.number_served}")
r_2.describe_restaurant()
r_2.open_restaurant()
r_2.increment_number_served()
print("")

"""Creating instance three(r_3) of class Restaurant"""
r_3 = Restaurant("Pizza Hut", "Italian", 50)
r_3.number_served = 60
r_3.set_number_served(61)
print(f"Restaurant Name: {r_3.restaurant_name}")
print(f"Cuisine Name: {r_3.cuisine_type}")
print(f"Number of Customers: {r_3.number_served}")
r_3.describe_restaurant()
r_3.open_restaurant()
r_3.increment_number_served()
print("")