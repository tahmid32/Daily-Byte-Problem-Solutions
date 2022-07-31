def valid_anagram(s, t):
    s_list = []
    t_list = []
    
    for char in s:
        if (char != ' '):
            s_list.append(char.lower())
            
    for char in t:
        if (char != ' '):
            t_list.append(char.lower())
            
    s_set = set(s_list)
    t_set = set(t_list)
    
    if (len(s_set.difference(t_set)) != 0):
        return False
    
    return True
