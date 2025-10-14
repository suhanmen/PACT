def search(lst):
    for i in range(1, max(lst)+1):
        freq = lst.count(i)
        if freq >= i and i > 0:
            return i
    return -1
