def search(lst):
    # Create a dictionary to keep track of the frequency of each integer
    freq_dict = {}
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    # Iterate through the dictionary and find the greatest integer that meets the criteria
    max_num = -1
    for num, freq in freq_dict.items():
        if num > 0 and freq >= num:
            if num > max_num:
                max_num = num
    
    return max_num
