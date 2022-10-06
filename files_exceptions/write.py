file_path = '/Users/Simran.Kaur6/Desktop/personal-projects/python3/files_exceptions/python.txt'

# Various different modes available 
# to read - 'r'
# to write - 'w'
# to append - 'a'
# to read/write - 'r+'
# if argument not provided exclusivly, python will open the file in read mode by default
with open(file_path, 'a') as file_object:
    file_object.write("\nI love programming in python \n")
    file_object.write(str(123456789))