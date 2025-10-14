def search(lst):
    freq_dict = {}
    max_num = -1
    for num in lst:
        if num > 0:
            freq_dict[num] = freq_dict.get(num, 0) + 1
    for num, freq in freq_dict.items():
        if freq >= num:
            max_num = max(max_num, num)
    return max_num
