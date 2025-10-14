def search(lst):
    frequency_dict = {}
    for num in lst:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1
    
    max_num = -1
    for num in frequency_dict:
        if num > 0 and num <= frequency_dict[num] and num > max_num:
            max_num = num
    
    return max_num
