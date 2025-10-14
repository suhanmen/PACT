def search(lst):
    freq_dict = {}
    for num in lst:
        if num not in freq_dict:
            freq_dict[num] = lst.count(num)
    max_num = -1
    for num, freq in freq_dict.items():
        if num > freq and freq > max_num:
            max_num = freq
    return max_num if max_num > -1 else -1
