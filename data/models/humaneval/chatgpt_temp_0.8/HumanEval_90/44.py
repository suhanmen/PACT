def next_smallest(lst):
    # Remove duplicates from the list
    unique_lst = list(set(lst))
    
    # Sort the list in ascending order
    sorted_lst = sorted(unique_lst)
    
    # If the list has at least two elements, return the second smallest element
    if len(sorted_lst) >= 2:
        return sorted_lst[1]
    else:
        return None
