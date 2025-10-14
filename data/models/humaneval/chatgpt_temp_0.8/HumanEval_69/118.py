def search(lst):
    for i in range(1, max(lst)+1):
        if lst.count(i) >= i and i > 0:
            return i
    return -1
