# storing values in a tuple which are immutable
menu = ("Toast", "Chicken", "Beans", "Ham", "Turkey")

for item in menu:
    print(f"Items in today's menu: {item}")
    
print("")

# Tuple can only be modified it the declaration is done all over again
menu = ("Toast", "Chicken", "Sandwich", "Cream of Broccli", "Turkey")

for item in menu:
    print(f"Revised Items in today's menu: {item}")


