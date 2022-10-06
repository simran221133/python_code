# for manually testing the input
from function_tc import get_formatted_name

print("Print 'q' at anytime to quit ")
while True:
    first_name = input("Enter your first name: ")
    if first_name == 'q':
        break
    middle_name = input("Enter your last name: ")
    if middle_name == 'q':
        break
    last_name = input("Enter your last name: ")
    if last_name == 'q':
        break

    formatted_name = get_formatted_name(first_name, middle_name, last_name)
    print(f"Formatted name: {formatted_name.title()}")