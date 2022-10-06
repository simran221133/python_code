def isPhoneNumber(string1):
    # check if the length of string1 is not equal to 12 ex:- 519-965-8615
    if len(string1) != 12:
        return False

    # checking if first three character are non-decimal/number values
    for i in range(0,3):
        if not string1[i].isdecimal():
            return False

    # checking if 4th character is a '-' as mentioned in phone number
    if string1[3] != "-":
        return False

    # checking if 4 to 7 characters are non-decimal/number values        
    for i in range(4,7):
        if not string1[i].isdecimal():
            return False

    # checking if 7th character is a '-' as mentioned in phone number
    if string1[7] != "-":
        return False
        
    # checking if 8 to 12 characters are non-decimal/number values
    for i in range(8,12):   
        if not string1[i].isdecimal():
            return False  
    return True
              
