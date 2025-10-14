def next_smallest(lst):
    if len(lst) < 2:
        return None
    else:
        lst = sorted(set(lst))
        if len(lst) < 2:
            return None
        else:
            return lst[1]
