def search(lst):
    # Create a dictionary to keep the frequency of each integer in the list
    freq = {}
    for num in lst:
        freq[num] = freq.get(num, 0) + 1
    
    # Iterate over the dictionary and find the first integer that meets the conditions
    for num, cnt in freq.items():
        if num > 0 and cnt >= num:
            return num
    
    # If no such integer is found, return -1
    return -1
