def reverse_string(str):
    char_lst = []
    for char in str:
        char_lst.append(char)
    
    start, stop = 0, (len(char_lst) - 1)
    while (start < stop):
        char_lst[start], char_lst[stop] = char_lst[stop], char_lst[start]
        start, stop = start+1, stop-1
    
    final_str = ""
    for char in char_lst:
        final_str += char
        
    return final_str
