# to load to load the data from a json file to the memory and print
import json

file_path = 'number.json'

with open(file_path, 'r') as f:
    # using json.load to load data from a json file(file_path) as f to local memory and print using a variable
    numbers = json.load(f)
    print(numbers)