def search(lst):
    # create a dictionary to store the frequency of each integer
    freq_dict = {}
    for num in lst:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    
    # iterate through the list to find the greatest integer that satisfies the condition
    max_integer = -1
    for num in lst:
        if num > max_integer and num <= freq_dict[num]:
            max_integer = num
    
    return max_integer
