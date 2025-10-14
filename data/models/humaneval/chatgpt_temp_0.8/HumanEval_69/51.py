def search(lst):
    # Create a dictionary to keep track of the frequency of each integer
    freq = {}
    for num in lst:
        freq[num] = freq.get(num, 0) + 1
        
    # Look for the greatest integer that meets the conditions
    result = -1
    for num in freq:
        if num > 0 and freq[num] >= num:
            result = max(result, num)
            
    return result
