def search(lst):
    freq_dict = {}
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    max_num = -1
    for num in freq_dict:
        if num > 0 and freq_dict[num] >= num:
            max_num = max(max_num, num)
    
    return max_num
