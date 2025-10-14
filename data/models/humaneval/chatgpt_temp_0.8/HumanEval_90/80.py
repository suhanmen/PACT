def next_smallest(lst):
    if len(lst) < 2:
        return None
    else:
        lst = list(set(lst)) # Remove duplicates
        lst.sort()
        if len(lst) < 2:
            return None
        else:
            return lst[1]
