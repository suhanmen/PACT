def search(lst):
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for key in sorted(freq, reverse=True):
        if key <= freq[key]:
            return key
    return -1
