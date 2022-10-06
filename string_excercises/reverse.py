# Reverse words in a given String in Python
word = input("Please input a string: ")

# : start at the end
# : end when nothing's left
# 1 walk backwads by 1
# https://towardsdatascience.com/the-basics-of-indexing-and-slicing-python-lists-2d12c90a94cf
print(f"Reversed string: {word[::-1]}")