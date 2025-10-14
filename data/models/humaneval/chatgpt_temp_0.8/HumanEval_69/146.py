def search(lst):
    counts = {}
    for num in lst:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
    result = -1
    for num in counts:
        if num > 0 and counts[num] >= num:
            result = max(result, num)
    return result
