def next_smallest(lst):
    if len(lst) < 2:
        return None
    
    # remove duplicates from the list
    unique_lst = list(set(lst))
    
    if len(unique_lst) < 2:
        return None
    
    # find the 2nd smallest element
    unique_lst.sort()
    return unique_lst[1]
