def search(lst):
    freq_dict = {}
    for num in lst:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    max_num = -1
    for key, value in freq_dict.items():
        if key == value and key > 0:
            max_num = max(max_num, key)
    return max_num
