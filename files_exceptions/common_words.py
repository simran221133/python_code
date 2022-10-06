file = '20_tales_by_20_women.txt'

with open(file) as f:
    contents = f.read()
    # using lower method to convert all text to lower case
    # using count method to count occurences of 'the'
    number_of_occurences = contents.lower().count('the ')
    print(number_of_occurences)
