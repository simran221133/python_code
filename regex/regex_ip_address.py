import re

# regular expression for matching 0 to 99
#### [0-9][0-9]?
# regular expression for matching 1 to 99
#### [1-9][0-9]?
# regular exprression for matching 100 to 199
#### 1[0-9][0-9]
# regular exprression for matching 200 to 249
#### 2[0-4][0-9]
# regular exprression for matching 249 to 255
#### 25[0-5]

regexfind = re.compile(r'^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9][0-9]?)$')

user_input = input("Validate IP Addresses here: ")

mo = regexfind.search(user_input)

if mo:
    print(f"This is a valid IP: {mo.group()}")
else:
    print("Invalid IP Address")