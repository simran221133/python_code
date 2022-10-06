file_path = '/Users/Simran.Kaur6/Desktop/personal-projects/python3/files_exceptions/random.txt'
with open(file_path) as file_object:
# readlines is a method to store the file_object as a list which can later be used out of the with block
    lines = file_object.readlines()

# looping through the list     
for line in lines:
    print(line.rstrip())

print(lines)
print(type(lines))