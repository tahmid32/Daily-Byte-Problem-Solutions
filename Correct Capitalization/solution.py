def correct_capitalization(str):
    if (str.isupper() == False):
        if (str[1:].islower() == False):
            return False
     
    return True           
