def search(lst):
    freq_dict = {}
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1

    max_freq = -1
    max_num = -1

    for num in freq_dict:
        if freq_dict[num] >= num and num > max_num:
            max_num = num
            max_freq = freq_dict[num]

    return max_num if max_freq > 0 else -1
