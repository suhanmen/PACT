def search(lst):
    freq = {}
    for num in lst:
        freq[num] = freq.get(num, 0) + 1
    
    max_val = -1
    for num, count in freq.items():
        if num == count and num > max_val:
            max_val = num
    
    return max_val
