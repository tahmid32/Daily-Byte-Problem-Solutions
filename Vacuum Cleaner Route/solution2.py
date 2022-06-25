def vacuum_cleaner(str):
    direction_dict = {'L' : 0, 'R': 0, 'U': 0, 'D': 0}
    
    for char in str:
        direction_dict[char] += 1
    
    if ((direction_dict['L'] == direction_dict['R']) and (direction_dict['U'] == direction_dict['D'])):
        return 'True'
    else:
        return 'False'
