def next_smallest(lst):
    if len(lst) < 2:
        return None
    else:
        lst = list(set(lst)) # remove duplicates
        lst.sort()
        if len(lst) > 1:
            return lst[1]
        else:
            return None
