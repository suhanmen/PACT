def search(lst):
    freq_dict = {}
    max_num = -1

    # count frequency of each number in lst
    for num in lst:
        if num > 0:
            if num not in freq_dict:
                freq_dict[num] = 1
            else:
                freq_dict[num] += 1

    # find the maximum number that satisfies the condition
    for num, freq in freq_dict.items():
        if freq >= num and num > max_num:
            max_num = num
            
    return max_num
