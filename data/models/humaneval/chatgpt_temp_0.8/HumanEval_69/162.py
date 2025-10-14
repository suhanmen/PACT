def search(lst):
    # Create a dictionary to store the frequency of each number
    freq_dict = {}
    for num in lst:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    
    # Iterate through the dictionary to find the greatest integer that satisfies the condition
    max_num = -1
    for num, freq in freq_dict.items():
        if num > 0 and freq >= num and num > max_num:
            max_num = num
    
    return max_num
