def next_smallest(lst):
    # discard duplicates
    lst = sorted(set(lst))
    # return 2nd smallest element if present
    return lst[1] if len(lst) > 1 else None
