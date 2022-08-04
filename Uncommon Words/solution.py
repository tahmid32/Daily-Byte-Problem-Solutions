def uncommon_words(sentence1, sentence2):
    sentence1_set = set(sentence1.split(" "))
    sentence2_set = set(sentence2.split(" "))
    
    difference_list = []
    
    for item in sentence1_set.symmetric_difference(sentence2_set):
        difference_list.append(item)
        
    return difference_list
