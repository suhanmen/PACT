def search(lst):
    max_num = -1
    for num in lst:
        freq = lst.count(num)
        if num > 0 and freq >= num and num > max_num:
            max_num = num
    return max_num
