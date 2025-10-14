def search(lst):
    # create a dictionary to store the frequency of each integer
    freq = {}
    for i in lst:
        freq[i] = freq.get(i, 0) + 1
    
    # iterate through the dictionary to find the greatest integer that meets the criteria
    result = -1
    for i in freq:
        if i > 0 and freq[i] >= i:
            result = max(result, i)
    
    return result
