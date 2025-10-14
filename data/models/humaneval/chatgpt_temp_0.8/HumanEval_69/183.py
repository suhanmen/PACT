def search(lst):
    nums = set(lst)
    res = -1
    for num in nums:
        freq = lst.count(num)
        if freq >= num and num > res:
            res = num
    return res
