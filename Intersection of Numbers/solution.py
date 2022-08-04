def intersection(nums1, nums2):
    intersection_list = []
    
    for item in set(nums1).intersection(set(nums2)):
        intersection_list.append(item)
    
    return intersection_list
