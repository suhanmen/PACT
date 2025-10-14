def search(lst):
    for num in sorted(set(lst), reverse=True):
        freq = lst.count(num)
        if freq >= num > 0:
            return num
    return -1
