def search(lst):
    freq_dict = {}
    max_val = -1
    for num in lst:
        if num not in freq_dict:
            freq_dict[num] = 1
        else:
            freq_dict[num] += 1
    for num, freq in freq_dict.items():
        if num == freq and num > max_val:
            max_val = num
    return max_val
