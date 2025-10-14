python
def search(lst):
    freq_dict = {}
    for num in lst:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    for num in sorted(freq_dict.keys(), reverse=True):
        if num > 0 and freq_dict[num] >= num:
            return num
    return -1
