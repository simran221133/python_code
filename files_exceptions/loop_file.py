file_path = '/Users/Simran.Kaur6/Desktop/personal-projects/python3/files_exceptions/random.txt'
with open(file_path) as file_object:
# looping through each line in file_object(which is the object of the file) 
    for line in file_object:
        print(line.rstrip())