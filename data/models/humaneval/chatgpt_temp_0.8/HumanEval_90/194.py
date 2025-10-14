def next_smallest(lst):
    # Remove duplicates and sort the list
    unique_lst = sorted(set(lst))
    
    # Return the second smallest element if it exists
    if len(unique_lst) > 1:
        return unique_lst[1]
    else:
        return None
