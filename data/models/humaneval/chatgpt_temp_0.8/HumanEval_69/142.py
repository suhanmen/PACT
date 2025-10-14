def search(lst):
    # Find the maximum value in the list
    max_val = max(lst)
    
    # Initialize a list to keep track of frequency of each integer
    freq = [0] * (max_val + 1)
    
    # Count the frequency of each integer
    for num in lst:
        freq[num] += 1
    
    # Search for the greatest integer that meets the conditions
    for i in range(1, max_val+1):
        if freq[i] >= i and i > 0:
            return i
    
    # If no such integer exists, return -1
    return -1
