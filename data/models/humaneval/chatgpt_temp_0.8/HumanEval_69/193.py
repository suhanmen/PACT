def search(lst):
    # create a dictionary to keep track of the frequency of each integer in the list
    freq_dict = {}
    for num in lst:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    
    # iterate through the dictionary and find the greatest integer that meets the conditions
    max_num = -1
    for num, freq in freq_dict.items():
        if num > 0 and freq >= num:
            max_num = max(max_num, num)
    
    return max_num
