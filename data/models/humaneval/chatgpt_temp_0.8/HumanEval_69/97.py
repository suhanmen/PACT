def search(lst):
    freq = {}
    for num in lst:
        freq[num] = freq.get(num, 0) + 1
    max_val = -1
    for num in freq:
        if num > 0 and freq[num] >= num:
            max_val = max(max_val, num)
    return max_val
