def search(lst):
    frequency = {}
    for num in lst:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    for num in sorted(frequency.keys(), reverse=True):
        if frequency[num] >= num and num > 0:
            return num
    
    return -1
