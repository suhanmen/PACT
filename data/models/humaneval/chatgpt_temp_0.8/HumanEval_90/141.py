def next_smallest(lst):
    if len(lst) < 2:
        return None
    else:
        sorted_list = sorted(set(lst))
        if len(sorted_list) < 2:
            return None
        else:
            return sorted_list[1]
