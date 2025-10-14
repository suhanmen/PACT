def search(lst):
    freq_dict = {}
    for num in lst:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    max_num = -1
    for num, freq in freq_dict.items():
        if num > freq and freq > max_num:
            max_num = freq
    return max_num if max_num != -1 else -1
