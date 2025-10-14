def search(lst):
    freq_dict = {}
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    max_freq = 0
    max_num = -1
    for num, freq in freq_dict.items():
        if num > max_freq and freq >= num:
            max_freq = freq
            max_num = num
    return max_num
