# 4-1
pizzas = ["pepperoni", "hawaian", "all-meat"]

for pizza in pizzas:
    print(f"I like {pizza} pizza.")

print("\nI really love PIZZA!!!")

# to copy the entire list 
friend_pizzas = pizzas[:]

# appending piizza to pizzas list
pizzas.append("Cheese")

# appending friend_piizza to pizzas list
friend_pizzas.append("Butter chicken")

# Print message for all pizzas in pizza list
for pizza in pizzas:
    print(f"My favorite pizzas are: {pizza}")
print("")

# Print message for all pizzas in friend_pizza list
for pizza in friend_pizzas:
    print(f"My friend's favorite pizzas are: {pizza}")