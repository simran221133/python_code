# for importing multiple class from a module

# 1. import each class specifically  
# Preferred 
# from car import Car, ElectricCar

# 2. import all classes in a module 
# NOTE :-(Not RECOMMENDED as it creates confusion of which class you are actually referring to)
# from car import *

# 3. or multiple classes can be imported using dot notation 
# Preferred 
# such as my_tesla = Car.ElectricCar("Tesla", "ModelS", 2022, 10)

# importing Car class from car(which is the file name)
from car import Car

# importing ElectricCar class(subclass of Car) from electric_car(which is the file name)
from electric_car import ElectricCar as EC

# as EC is used to assign an aliase to the ElectricCar class

"""Creating instance one(car1) of class Car"""
c1 = Car("Honda", "Civic", 2020, 10)
c1.get_descriptive_name()
c1.update_odmeter(0)
print(f"")

"""Creating instance two(car2) of class Car"""
c2 = Car("Toyota", "Corolla", 2019, 56780)
c2.get_descriptive_name()
c2.update_odmeter(70000)
print(f"")

"""Creating instance three(car3) of class Car"""
c3 = Car("Hyundai", "Elantra", 2022, 1070)
c3.get_descriptive_name()
c3.update_odmeter(1050)
print(f"")

"""Creating instance four(car4) of class Car"""
c4 = Car("Kia", "Forte", 2021, 76890)
c4.get_descriptive_name()
c4.update_odmeter(100000)
print(f"")

"""Creating instance five(car5) of class ElectricCar which is a subclass of Car"""
my_tesla = EC("Tesla", "ModelS", 2022, 10)
my_tesla.get_descriptive_name()
my_tesla.battery_info()
my_tesla.upgrade_battery()
my_tesla.upgrade_battery()
my_tesla.upgrade_battery()


