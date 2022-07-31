def first_unique(string):
    string_len = len(string)
    duplicate_list = []
    
    for i in range(string_len):
        for j in range(i+1, string_len):
            if (string[i] == string[j]):
                duplicate_list.append(string[i])
                break
            
        if ((string[i] not in duplicate_list)):
            return i
    
    return -1
