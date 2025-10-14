def search(lst):
    freq_dict = {}
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    for num, freq in freq_dict.items():
        if freq >= num and num > 0:
            return max([key for key, value in freq_dict.items() if value >= key])
    return -1
