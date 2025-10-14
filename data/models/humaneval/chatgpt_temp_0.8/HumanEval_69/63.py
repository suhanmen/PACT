def search(lst):
    freq_dict = {} # create an empty dictionary to store the frequency of each integer
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    max_freq = -1
    max_num = -1
    for num, freq in freq_dict.items():
        if num <= freq and freq > max_freq:
            max_freq = freq
            max_num = num
    
    return max_num
