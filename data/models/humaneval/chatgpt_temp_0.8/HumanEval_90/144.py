def next_smallest(lst):
    if len(lst) < 2:
        return None
    lst = sorted(set(lst))
    if len(lst) < 2:
        return None
    return lst[1]
