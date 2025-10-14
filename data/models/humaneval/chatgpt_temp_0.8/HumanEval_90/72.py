def next_smallest(lst):
    # Remove duplicates and sort in ascending order
    sorted_lst = sorted(set(lst))
    
    if len(sorted_lst) < 2:
        # There are less than 2 unique elements in the list
        return None
    else:
        # Return the second smallest element
        return sorted_lst[1]
