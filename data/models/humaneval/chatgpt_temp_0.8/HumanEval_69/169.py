def search(lst):
    freq_dict = {}
    # create a dictionary to store the frequency of each integer in the list
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    # loop through the dictionary to find the greatest integer that meets the conditions
    max_val = -1
    for num, freq in freq_dict.items():
        if num > freq and freq > max_val:
            max_val = freq
    
    return max_val if max_val != -1 else -1
