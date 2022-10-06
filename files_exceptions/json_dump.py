# using json dump to dump data from a list to a json file
import json

# list of numbers
number = [1, 3, 5, 7, 9, 11, 13, 15]

file_name = 'number.json'
with open(file_name, 'w') as f:
    # using json.dump to copy data from list to a json file
    json.dump(number, f)