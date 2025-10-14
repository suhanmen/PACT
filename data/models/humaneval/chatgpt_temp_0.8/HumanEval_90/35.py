def next_smallest(lst):
    if len(lst) < 2:  # if the list has less than 2 elements, there is no second smallest
        return None
    
    # sort the list and return the second element
    sorted_lst = sorted(set(lst))  # set() is used to remove duplicates before sorting
    return sorted_lst[1]
