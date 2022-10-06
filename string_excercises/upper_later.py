# Uppercase Half String
# Given a String, perform uppercase of later part of string.

string = input("Input a random string: ")

mid = round(int(len(string)/2))
mid = int(mid)

string1 = string.split()

list1 = []

for s in string1:
    if s in range(mid, len(string)):
        s = s.upper()
        list1.append(s)
    else:
        list1.append(s)


print(list1)





