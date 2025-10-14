def search(lst):
    # create a dictionary to store the frequency of each integer in the list
    freq_dict = {}
    for num in lst:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    
    # loop through the dictionary and find the greatest integer 
    # that has a frequency greater than or equal to the value of the integer itself
    max_num = -1
    for num, freq in freq_dict.items():
        if num > 0 and freq >= num:
            max_num = max(max_num, num)
    
    # return the result
    return max_num
