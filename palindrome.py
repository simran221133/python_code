def pal(num):
    num = list(num)
    x = num[::-1]
    if num == x:
        print("Palindrome")
    else:
        print("Not a Palindrome")
