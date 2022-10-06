# WITH keyword helps python close and open a file
# OPEN function to open a file provided as an argument
# file_object is the object of the file
# read is a method to read the contents of a file

file_path = '/Users/Simran.Kaur6/Desktop/personal-projects/python3/files_exceptions/random.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)
    