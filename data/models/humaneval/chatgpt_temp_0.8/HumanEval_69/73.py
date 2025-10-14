def search(lst):
    # Initialize a dictionary to store the frequency of each integer in the list
    freq_dict = {}
    for num in lst:
        freq_dict[num] = freq_dict.get(num, 0) + 1

    # Iterate over the dictionary and find the greatest integer that meets the condition
    max_int = -1
    for num, freq in freq_dict.items():
        if num > 0 and freq >= num and num > max_int:
            max_int = num

    return max_int
