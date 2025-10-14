def search(lst):
    freq = {}
    for x in lst:
        if x > 0:
            freq[x] = freq.get(x, 0) + 1
    max_val = -1
    for x, f in freq.items():
        if x <= f and f > max_val:
            max_val = f
    return max_val if max_val > -1 else -1
