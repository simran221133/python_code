def isIPAddress(string1):
    # check if the length of string1 is not equal to 12 ex:- 519-965-8615

    new_list = string1.split(".")
    if new_list[0] == '0':
        return False
    else: 
        for item in new_list:
            if int(item)>=0 and int(item)<=255:
                print("Valid octat")
            else:
                print("Not a valid octat")        
        return False
    return True
