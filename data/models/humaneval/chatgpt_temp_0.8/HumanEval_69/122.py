def search(lst):
    # Create a dictionary to store the frequency of each integer
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    # Check each integer in the dictionary
    result = -1
    for num, f in freq.items():
        if num > 0 and f >= num:
            if num > result:
                result = num
    
    return result
