def next_smallest(lst):
    if len(lst) < 2:
        return None
    
    unique_lst = sorted(set(lst))
    if len(unique_lst) < 2:
        return None
    
    return unique_lst[1]
