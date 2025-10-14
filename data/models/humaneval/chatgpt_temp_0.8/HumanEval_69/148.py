def search(lst):
    # Create a dictionary to store the frequency of each integer
    freq_dict = {}
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    # Find the integer with a frequency greater than or equal to its value
    max_int = -1
    for num, freq in freq_dict.items():
        if num > 0 and freq >= num:
            if num > max_int:
                max_int = num
    
    return max_int
