def search(lst):
    nums = set(lst)
    max_freq = 0
    result = -1
    for num in nums:
        freq = lst.count(num)
        if num == freq and freq > max_freq:
            max_freq = freq
            result = num
    return result
