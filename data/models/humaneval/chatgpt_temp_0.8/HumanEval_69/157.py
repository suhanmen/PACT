def search(lst):
    # Create a dictionary to count the frequency of each integer
    freq = {}
    for num in lst:
        freq[num] = freq.get(num, 0) + 1
    
    # Loop through the integers in descending order
    for num in sorted(freq.keys(), reverse=True):
        # Check if the frequency is greater than or equal to the integer value
        if freq[num] >= num and num > 0:
            return num
    
    # If no such integer is found, return -1
    return -1
