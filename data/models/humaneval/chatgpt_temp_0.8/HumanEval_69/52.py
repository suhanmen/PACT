def search(lst):
    # create a frequency dictionary of the list
    freq_dict = {}
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    # check for the greatest value with frequency greater than or equal to the value itself
    max_val = -1
    for num in freq_dict:
        if freq_dict[num] >= num and num > 0:
            if num > max_val:
                max_val = num
    
    return max_val
