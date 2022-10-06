# Ways to remove i’th character from string in Python
string = input("Insert a string: ")

i = input("Insert the character to be removed: ")

new = ""

for char in string:
    if char != i:
        new = new + char

print(f"Updated string {new}")

# or use string.replace("a", "", 1)
# removing only the first occurence of "a"
        