def correct_capitalization(str):
    if (str[0].islower() == True):
        if (str[1:].islower() == False):
            return False
        """
        for char in str[1:]:
            if (char.islower() == False):
                return False
        """
        
    else:
        if ((str[1:].isupper() == False) and (str[1:].islower() == False)):
            return False
        """
        if (str[1].isupper() == True):
            for char in str[2:]:
                if (char.isupper() == False):
                    return False
        
        else:
            for char in str[2:]:
                if (char.islower() == False):
                    return False
        """    
    return True
