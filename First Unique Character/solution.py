def first_unique(string):
    count_dict = {}
    first_unique_char = ''
    
    for char in string:
        count_dict[char] = count_dict.get(char, 0) + 1
          
    for key, value in count_dict.items():
        if (value == 1):
            first_unique_char = key
            break
    
    if (first_unique_char == ''):
        return -1
    else:
        return string.index(first_unique_char)
