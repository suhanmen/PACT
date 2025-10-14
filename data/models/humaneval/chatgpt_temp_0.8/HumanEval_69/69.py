def search(lst):
    freq_dict = {}
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    result = -1
    for num in freq_dict:
        if freq_dict[num] >= num and num > 0:
            if num > result:
                result = num
    return result
