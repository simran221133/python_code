# Python program to print even length words in a string

sentence = input("Insert a sentence: ")
# spliting the sentence into list
new_list = sentence.split(" ")
new = []

for word in new_list:
    if len(word)%2 == 0:
        new.append(word)

# whitespace to append between the words from the list
str1 = " "
# using join function to join words from list with whitespaces
new_sentence = str1.join(new)
print(new_sentence)