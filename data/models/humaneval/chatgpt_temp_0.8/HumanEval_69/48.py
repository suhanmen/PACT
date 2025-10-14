def search(lst):
    freq_dict = {}
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    max_val = -1
    for key, val in freq_dict.items():
        if key > 0 and val >= key and key > max_val:
            max_val = key
    return max_val
