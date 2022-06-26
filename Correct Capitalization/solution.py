def correct_capitalization(str):
    if (str.isupper() == True):
        return True
    else:
        if (str[1:].islower() == True):
            return True
        else:
            return False
           
