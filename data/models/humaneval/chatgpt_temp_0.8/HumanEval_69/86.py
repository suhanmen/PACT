def search(lst):
    freq_dict = {}
    for num in lst:
        freq_dict[num] = freq_dict.get(num, 0) + 1

    max_val = -1
    for num, freq in freq_dict.items():
        if num > freq and freq > max_val:
            max_val = freq

    if max_val == -1:
        return -1

    for num, freq in freq_dict.items():
        if freq == max_val and num > max_val:
            return num

    return -1
