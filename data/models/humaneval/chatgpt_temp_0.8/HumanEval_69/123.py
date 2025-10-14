def search(lst):
    # Create a dictionary to count the frequency of each integer in the list
    freq_dict = {}
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    # Loop through the dictionary to find the greatest integer that meets the condition
    max_val = -1
    for num, freq in freq_dict.items():
        if num > 0 and freq >= num:
            max_val = max(max_val, num)
    
    return max_val
