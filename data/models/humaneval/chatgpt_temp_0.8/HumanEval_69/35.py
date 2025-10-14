def search(lst):
    freq_dict = {}
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    for num in sorted(freq_dict.keys(), reverse=True):
        if num <= freq_dict[num]:
            return num
    return -1
