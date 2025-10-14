def search(lst):
    # Create a dictionary to store the frequency of each integer in the list
    freq_dict = {}
    for num in lst:
        freq_dict[num] = freq_dict.get(num, 0) + 1

    # Iterate through the dictionary to find the greatest integer that meets the criteria
    max_int = -1
    for num, freq in freq_dict.items():
        if num > 0 and freq >= num:
            max_int = max(max_int, num)

    return max_int
