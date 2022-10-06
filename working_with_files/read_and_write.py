file_name = "/Users/Simran.Kaur6/Desktop/personal-projects/python3/working_with_files/user_input.txt"
user_input = input("Please enter a sentence: ")

with open(file_name, 'a') as file_object:
    file_object.write("\n")
    file_object.write(user_input)

with open(file_name, 'r') as file_object:
    input1 = file_object.read()
    print(input1)

