# importing phone_number function from isPhoneNumber file
from phone_number import isPhoneNumber

# take user input to return phone numbers
user_input = input("Please insert a phone number: ")

for i in range(len(user_input)):
    # set a string call chunk with multiples of 12, ex:- 0,12 or 1,13 or 2,14
    chunk = user_input[i:i+12]

    # calling isPhoneNumber function on the part of string called 'chunk'
    if isPhoneNumber(chunk):
        print(f"This is a valid phone number: {chunk}")
print("Done!")