def next_smallest(lst):
    if len(lst) < 2:
        return None
    
    unique_lst = list(set(lst))
    if len(unique_lst) < 2:
        return None
    
    sorted_lst = sorted(unique_lst)
    return sorted_lst[1]
