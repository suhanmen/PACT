def search(lst):
    # Create a frequency dictionary for all the numbers in the list
    freq_dict = {}
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    # Find the greatest integer with frequency greater than or equal to itself
    greatest_num = -1
    for num, freq in freq_dict.items():
        if freq >= num and num > greatest_num:
            greatest_num = num
    
    return greatest_num
