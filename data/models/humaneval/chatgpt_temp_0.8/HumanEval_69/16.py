def search(lst):
    freq = {}
    for i in lst:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    result = -1
    for i, count in freq.items():
        if i > count and count > result:
            result = count
    return result
