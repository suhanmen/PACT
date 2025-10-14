def next_smallest(lst):
    if len(lst) < 2:
        return None
    else:
        # sort the list in ascending order
        sorted_lst = sorted(set(lst))
        if len(sorted_lst) < 2:
            return None
        else:
            return sorted_lst[1]
