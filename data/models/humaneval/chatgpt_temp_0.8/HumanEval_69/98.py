def search(lst):
    freq_dict = {}
    for num in lst:
        if num not in freq_dict:
            freq_dict[num] = lst.count(num)
    for key in sorted(freq_dict.keys(), reverse=True):
        if key <= freq_dict[key]:
            return key
    return -1
