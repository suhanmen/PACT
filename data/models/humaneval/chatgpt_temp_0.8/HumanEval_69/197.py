def search(lst):
    frequency_dict = {}
    for num in set(lst):
        frequency_dict[num] = lst.count(num)
    result = -1
    for num, freq in frequency_dict.items():
        if num <= freq > result:
            result = num
    return result
