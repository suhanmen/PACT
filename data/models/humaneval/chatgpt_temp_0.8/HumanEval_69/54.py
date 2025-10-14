def search(lst):
    freq = {}
    for n in lst:
        freq[n] = freq.get(n, 0) + 1
    for n in sorted(freq.keys(), reverse=True):
        if freq[n] >= n and n > 0:
            return n
    return -1
