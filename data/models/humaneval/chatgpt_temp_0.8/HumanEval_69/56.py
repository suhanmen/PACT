python
def search(lst):
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    max_num = -1
    for key, value in freq.items():
        if key > 0 and value >= key:
            if key > max_num:
                max_num = key
    
    return max_num
