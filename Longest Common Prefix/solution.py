def longest_common_prefix(str_lst):
    prefix_track = []
    result_str = ""
    
    for char in str_lst[0]:
        prefix_track.append(char)
    
    for str in str_lst[1:]:
        iter_len = min(len(str), len(prefix_track))
        for i in range(iter_len):
            if (prefix_track[i] != str[i]):
                prefix_track = prefix_track[:i]
                break
                
            if (i == (iter_len - 1)):
                prefix_track = prefix_track[:i+1]
        
            
    for char in prefix_track:
        result_str += char
        
    return result_str
