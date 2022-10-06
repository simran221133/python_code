import json

user_input = input("Input a list of fruits: ")
file_path = "fruits.json"

with open(file_path, 'w') as file_object:
    json.dump(user_input, file_object)

with open(file_path, 'r') as file_object:
    output = json.load(file_object)
    print(output)