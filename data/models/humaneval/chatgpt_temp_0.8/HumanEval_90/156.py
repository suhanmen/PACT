def next_smallest(lst):
    if len(lst) < 2:
        return None
    elif len(set(lst)) == 1:
        return None
    else:
        return sorted(set(lst))[1]
