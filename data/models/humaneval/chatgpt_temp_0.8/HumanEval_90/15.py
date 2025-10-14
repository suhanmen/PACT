def next_smallest(lst):
    # If the list has less than 2 elements or contains duplicates, return None
    if len(set(lst)) < 2:
        return None
    
    # Sort the list and return the second element
    sorted_lst = sorted(lst)
    return sorted_lst[1]
