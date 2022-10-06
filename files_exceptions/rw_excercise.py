# 10-3
file_path = '/Users/Simran.Kaur6/Desktop/personal-projects/python3/files_exceptions/names.txt'
name1 = input("Please insert your name: ")

with open(file_path, 'a') as file_object:
    file_object.write(name1)
    file_object.write("\n")

# 10-4
file_path = '/Users/Simran.Kaur6/Desktop/personal-projects/python3/files_exceptions/guest_book.txt'
name2 = input("Please insert your name: ")

with open(file_path, 'a') as file_object:
    while name2:
        file_object.write(f"Hi {name2}... This is a test run\n")
        break
print(f"Hi {name2}... This is a sample message")

# 10-5
file_path = '/Users/Simran.Kaur6/Desktop/personal-projects/python3/files_exceptions/reasons.txt'
reason = input("Why do you like programming? - ")

with open(file_path, 'a') as file_object:
    while reason:
        file_object.write(f"{reason}\n")
        break
