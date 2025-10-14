def search(lst):
    freq_dict = {}
    for num in lst:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    result = -1
    for num, freq in freq_dict.items():
        if num > freq and freq > result:
            result = freq
    return result
