def search(lst):
    frequencies = {}
    for num in lst:
        if num in frequencies:
            frequencies[num] += 1
        else:
            frequencies[num] = 1
    
    max_num = -1
    for num, freq in frequencies.items():
        if freq >= num and num > max_num:
            max_num = num
    
    return max_num
