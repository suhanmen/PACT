def search(lst):
    freq_dict = {}
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    max_value = -1
    for num in freq_dict:
        if num == freq_dict[num] and num > max_value:
            max_value = num
    
    return max_value
