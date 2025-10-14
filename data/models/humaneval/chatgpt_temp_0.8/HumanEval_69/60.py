def search(lst):
    for i in range(1, max(lst)+1):
        if lst.count(i) >= i:
            return i
    return -1
