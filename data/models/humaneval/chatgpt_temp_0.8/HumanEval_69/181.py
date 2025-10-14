def search(lst):
    max_num = max(lst)
    freq_dict = {}
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    for i in range(1, max_num+1):
        if i in freq_dict and freq_dict[i] >= i:
            return i
    return -1
