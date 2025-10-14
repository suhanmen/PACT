def search(lst):
    counts = {}
    for num in lst:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    for num, freq in counts.items():
        if num > 0 and freq >= num:
            return num
    return -1
