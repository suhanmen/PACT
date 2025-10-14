def search(lst):
    freq_dict = {}
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    max_int = -1
    for num, freq in freq_dict.items():
        if num > freq and freq > max_int:
            max_int = freq
    
    return max_int
