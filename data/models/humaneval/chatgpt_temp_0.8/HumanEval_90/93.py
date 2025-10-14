def next_smallest(lst):
    if len(lst) < 2:
        return None
    else:
        # remove duplicates and sort the list
        lst = sorted(list(set(lst)))
        if len(lst) > 1:
            return lst[1]
        else:
            return None
