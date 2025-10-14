def search(lst):
    # Create a dictionary to store the frequency of each integer in the list
    freq = {}
    for num in lst:
        freq[num] = freq.get(num, 0) + 1
    
    # Iterate over the dictionary items and find the desired integer
    target = -1
    for num, f in freq.items():
        if num > 0 and f >= num:
            if num > target:
                target = num
    
    return target
