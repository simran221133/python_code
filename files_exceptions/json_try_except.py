# this program dumps username to a names.json file and loads the name from memory
import json

file_path = 'names.json'

# try block to open a file and load username 
try:
    with open(file_path, 'r') as f:
        name = json.load(f)
# if the file is not found, ask user for his/her name and 
except FileNotFoundError:
    name = input("Hi user! What is your name? ")
    with open(file_path, 'w') as f:
        json.dump(name, f)
        print(f"Hi {name}! Welcome to Python Programming.")
# if the try block succeeds print welcome back message for the user
else:
    print(f"Hi {name}! Welcome Back...")


