def first_unique(string):
    count_dict = {}
    
    for char in string:
        count_dict[char] = count_dict.get(char, 0) + 1
          
    for key, value in count_dict.items():
        if (value == 1):
            return string.index(key)
    
    return -1
