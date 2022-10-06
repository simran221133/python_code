import csv

user_inputs = input("Input a list: ")
new_list = user_inputs.split(",")

file = open("csv_input.csv", 'w', newline='')
write_file = csv.writer(file)

for item in new_list:
    write_file.writerow(item)

