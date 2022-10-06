num1 = input("Input a random number1 or q to quit: ")
num2 = input("Input a random number2 or q to quit: ")

# while loop to check the user values and quit if required
while True:
    # checks if num1 is equal to q and break
    if num1 == 'q':
        break
    # checks if num2 is equal to q and break
    if num2 == 'q':
        break
    # added try/except block where there's a possibility of the code to crash
    try:
        quotient = int(num1)/int(num2)
    # except block to catch any exceptions that the try block has
    except ZeroDivisionError:
        print("Number2 cannot be zero")
        break
    # if the try block succeeds the else block is executed
    else:
        print(f"Number1 divided by number2: {quotient}")
