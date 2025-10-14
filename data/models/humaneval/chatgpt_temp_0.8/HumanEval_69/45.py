def search(lst):
    freq = {}
    for num in lst:
        if num > 0:
            freq[num] = freq.get(num, 0) + 1
    max_num = -1
    for num, f in freq.items():
        if num <= f:
            max_num = max(max_num, num)
    return max_num
