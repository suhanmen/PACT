def search(lst):
    freqs = {}
    for num in lst:
        if num in freqs:
            freqs[num] += 1
        else:
            freqs[num] = 1
    result = -1
    for num, freq in freqs.items():
        if num == freq and num > 0:
            if result == -1:
                result = num
            elif num > result:
                result = num
    return result
