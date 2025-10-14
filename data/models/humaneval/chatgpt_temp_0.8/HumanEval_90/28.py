def next_smallest(lst):
    if len(lst) < 2:  # if the list is empty or has only one element
        return None
    
    # remove duplicates
    lst = list(set(lst))
    
    if len(lst) < 2:  # if the list contains only one distinct element
        return None
    
    # sort the list and return the second smallest element
    lst.sort()
    return lst[1]
