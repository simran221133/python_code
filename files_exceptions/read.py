# 10-1
file_path = '/Users/Simran.Kaur6/Desktop/personal-projects/python3/files_exceptions/python.txt'

# print the contents once by reading the entire file
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)
    print("")

# print the contents once by looping over the file object
with open(file_path) as file_object:
    for line in file_object:
        print(line.strip())
    print("")

# once by storing the lines in a list and then working with them outside the with block
with open(file_path) as file_object:
    values = file_object.readlines()


# to replace all occurences of python with Py
xx = [value.replace('python', 'Py') for value in values if 'python' in value]
yy = [x.strip() for x in xx]
for y in yy:
    print(y)


