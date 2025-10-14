def search(lst):
    # create a dictionary to keep track of frequency of integers
    freq_dict = {}
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    # check for greatest integer with frequency greater or equal to itself
    max_freq = -1
    for num in freq_dict:
        if freq_dict[num] >= num and num > max_freq:
            max_freq = num
    
    return max_freq
