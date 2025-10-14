def search(lst):
    '''Returns the greatest integer that is greater than zero, and has a frequency
    greater than or equal to the value of the integer itself. If no such a value exist,
    return -1.
    '''
    freq_dict = {} # create an empty dictionary to store the frequency of each integer
    for i in lst:
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1
    
    max_val = -1 # initialize the max_val to -1
    for key, val in freq_dict.items():
        if key > val and key > max_val:
            max_val = key
    
    return max_val
