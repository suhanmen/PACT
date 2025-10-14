def search(lst):
    freq_dict = {}
    for num in lst:
        if num not in freq_dict:
            freq_dict[num] = lst.count(num)
    result = -1
    for num, freq in freq_dict.items():
        if num > freq and freq > result:
            result = freq
    return result
