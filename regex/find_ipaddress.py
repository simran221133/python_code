# importing phone_number function from isPhoneNumber file
from ip_address import isIPAddress

# take user input to return phone numbers
user_input = input("Please insert an IP address: ")

if isIPAddress(user_input):
    print(f"This is a valid IP address: {user_input}")
else:
    print(f"Not a valid IP: {user_input}")