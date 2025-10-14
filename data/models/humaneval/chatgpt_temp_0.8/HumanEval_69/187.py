def search(lst):
    # create a dictionary to store the frequency of each integer in the list
    freq_dict = {}
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    # loop through the dictionary and find the first integer that meets the condition
    for num in sorted(freq_dict.keys(), reverse=True):
        if freq_dict[num] >= num and num > 0:
            return num
    
    # no integer meets the condition, return -1
    return -1
