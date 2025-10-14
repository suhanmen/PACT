def search(lst):
    freq = {}
    for i in lst:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    max_num = -1
    for k, v in freq.items():
        if k > 0 and v >= k:
            max_num = max(max_num, k)
    return max_num
