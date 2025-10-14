def search(lst):
    freq_dict = {}
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
            
    max_frequency = 0
    result = -1
    for num, frequency in freq_dict.items():
        if num == frequency and num > max_frequency:
            max_frequency = num
            result = num
            
    return result
