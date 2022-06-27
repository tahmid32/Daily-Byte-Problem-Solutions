def valid_palindrome(str):
    char_lst = []
    
    for char in str:
        if (char.isalpha() == True):
            char_lst.append(char)
            
    for i in range(len(char_lst) // 2):
        if (char_lst[i].lower() != char_lst[-(i + 1)].lower()):
            return False
            
    return True
