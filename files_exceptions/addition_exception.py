# 10-6
while True:
    try:
        number1 = int(input("Enter one number: "))
        number2 = int(input("Enter another number: "))
    except ValueError:
        # catches exception for anything other than numbers
        print("Please insert a number instead of characters")
    else:
        result = number1 + number2
        print(result)
        break