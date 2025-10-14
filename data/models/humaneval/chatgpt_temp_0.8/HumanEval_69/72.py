def search(lst):
    frequencies = {}
    for i in lst:
        if i in frequencies:
            frequencies[i] += 1
        else:
            frequencies[i] = 1
    result = -1
    for key, value in frequencies.items():
        if key > 0 and value >= key:
            result = max(result, key)
    return result
