birthday = input("Insert your birthday in ddmmyyyy format - ")

file_path = '/Users/Simran.Kaur6/Desktop/personal-projects/python3/files_exceptions/random.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    if birthday in contents:
        print("Your birthday is present the file!")
    else:
        print("Your birthday not present in the file!")