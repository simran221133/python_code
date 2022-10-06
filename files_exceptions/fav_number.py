# 10-11
# input favorite number from user
import json

file_path = 'favorite_number.json'

try:
    # to load the favorite number from the file object
    with open(file_path, 'r') as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    # if the favorite number doesn't exist already, ask user for the number
    with open(file_path, 'w') as f:
        favorite_number = input("What is your favorite number?")
        json.dump(favorite_number, f)
        print("Your favorite number is stored.")
else:
    # dispaly the favorite number if try block succeeds 
    print(f"I know your favorite number! It's {favorite_number}")
