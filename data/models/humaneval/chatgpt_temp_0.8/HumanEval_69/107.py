def search(lst):
    counts = {}
    for num in lst:
        counts[num] = counts.get(num, 0) + 1
    for num, count in sorted(counts.items(), reverse=True):
        if count >= num > 0:
            return num
    return -1
