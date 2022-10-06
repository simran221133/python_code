import re

# variable to set the regex using re.compile
test_regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')

user_input = input("Please insert a string for searching the phone-numbers: ")
# variable to search the string for regex set above
mo = test_regex.search(user_input)

# variable to print the match item from the string 
print(f"Phone Number in the string: {mo.group()}")

# assigning areaCode to mo.group(1) & mainNumber to mo.group(2)
areaCode, mainNumber = mo.groups()
# variable to print group one from regex 
print(f"Area Code: {areaCode}")
# variable to print group two from regex
print(f"Phone Number: {mainNumber}")
