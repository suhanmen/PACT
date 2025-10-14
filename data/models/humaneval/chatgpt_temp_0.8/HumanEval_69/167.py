def search(lst):
    for i in range(max(lst), 0, -1):
        if lst.count(i) >= i:
            return i
    return -1
