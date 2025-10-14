def search(lst):
    # Create a dictionary to store the frequency of each integer in the list
    freq = {}
    for num in lst:
        freq[num] = freq.get(num, 0) + 1
    
    # Check each integer in the list
    max_num = -1
    for num, f in freq.items():
        if num > 0 and f >= num:
            max_num = max(max_num, num)
    
    return max_num
