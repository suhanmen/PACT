def search(lst):
    freq_dict = {}
    for num in lst:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    max_num = -1
    for num, freq in freq_dict.items():
        if num > 0 and freq >= num:
            max_num = max(max_num, num)
    return max_num
