def search(lst):
    counts = {}
    for num in lst:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    max_num = -1
    for num, count in counts.items():
        if num > 0 and count >= num:
            if num > max_num:
                max_num = num
    
    return max_num
