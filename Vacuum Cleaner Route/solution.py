def vacuum_cleaner(str):
    sum = 0
    for char in str:
        if (char == 'L'):
            sum += 1
        elif (char == 'R'):
            sum += -1
        elif (char == 'U'):
            sum += 1
        elif (char == 'D'):
            sum += -1
            
    if (sum == 0):
        return 'True'
    else:
        return 'False'
            
