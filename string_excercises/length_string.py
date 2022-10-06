# Find length of a string in python (4 ways)
# using len() function

string = input("Insert a random string:")

length = len(string)

print(f"Length of string {length}")

# using replace function to replace whitespaces with nothing ""
string = string.replace(" ", "")
print(f"Length of string without whitespaces: {len(string)}")