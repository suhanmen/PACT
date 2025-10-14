def search(lst):
    max_int = -1
    for i in set(lst):
        if i > 0 and lst.count(i) >= i:
            max_int = max(max_int, i)
    return max_int
