# Python program to check if a string has at least one letter and one number

from sre_compile import isstring


string = input("Insert a string: ")

while True:
    if isstring(string):
        print("string in correct format")
        break
    else:
        print("Try Again")
        