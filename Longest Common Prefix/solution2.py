def longest_common_prefix(str_lst):
    prefix_track = []
    result_str = ""
    
    str_lst.sort()
    
    for char in str_lst[0]:
        prefix_track.append(char)
    
    for str in str_lst[1:]:
        for i in range(len(prefix_check):
            if (prefix_track[i] != str[i]):
                prefix_track = prefix_track[:i]
                break
        
    for char in prefix_track:
        result_str += char
        
    return result_str
