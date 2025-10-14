def search(lst):
    freq = {}
    for num in lst:
        if num not in freq:
            freq[num] = 0
        freq[num] += 1
    for num in sorted(freq.keys(), reverse=True):
        if freq[num] >= num and num > 0:
            return num
    return -1
