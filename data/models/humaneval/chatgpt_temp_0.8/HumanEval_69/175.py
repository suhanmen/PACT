def search(lst):
    # Create a dictionary to store the frequency of each integer in the list
    freq = {}
    for num in lst:
        freq[num] = freq.get(num, 0) + 1
    
    # Iterate through all positive integers from 1 to the maximum value in the list
    for i in range(1, max(lst) + 1):
        # Check if the frequency of i is greater than or equal to i
        if freq.get(i, 0) >= i:
            return i
    
    # If no such integer exists, return -1
    return -1
