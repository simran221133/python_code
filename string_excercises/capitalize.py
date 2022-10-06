# Python program to capitalize the first and last character of each word in a string

string = input("Insert a sentence: ")

words = string.split(" ")

new_list = [word[0].title() + word[1:-1] + word[-1].title() for word in words]
print(new_list)


