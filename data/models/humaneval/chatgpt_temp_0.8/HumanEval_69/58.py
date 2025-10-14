def search(lst):
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
            
    max_freq = 0
    max_num = -1
    for num in freq:
        if num == freq[num] and num > max_freq:
            max_freq = num
            max_num = num
            
    return max_num
