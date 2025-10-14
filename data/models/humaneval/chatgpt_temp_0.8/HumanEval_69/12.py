def search(lst):
    count = {}
    for num in lst:
        if num > 0:
            count[num] = count.get(num, 0) + 1
    max_freq = -1
    max_num = -1
    for num, freq in count.items():
        if freq >= num and freq > max_freq:
            max_freq = freq
            max_num = num
    return max_num
