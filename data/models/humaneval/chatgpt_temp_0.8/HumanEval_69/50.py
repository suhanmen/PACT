def search(lst):
    freq_dict = {}
    for i in lst:
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1
    max_val = -1
    for key, val in freq_dict.items():
        if key == val and key > max_val:
            max_val = key
    return max_val
