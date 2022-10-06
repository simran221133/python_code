# Python program to check whether the string is Symmetrical or Palindrome
# example of palindromes = mama, khokho, dada

user_input = input("Input a string: ")

mid = round(len(user_input)/2)
first_half = user_input[:mid]
second_half = user_input[mid:]

if first_half == second_half:
    print("User entered a palindrome")
else:
    print("Not a palindrome")
