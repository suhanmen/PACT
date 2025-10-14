def next_smallest(lst):
    if len(lst) < 2: # if the list has fewer than 2 elements
        return None   # then there is no 2nd smallest element, so return None
    else:
        sorted_lst = sorted(set(lst)) # remove duplicates and sort the list
        if len(sorted_lst) < 2: # if there is only 1 unique element left
            return None   # then there is no 2nd smallest element, so return None
        else:
            return sorted_lst[1] # return the 2nd element in the sorted list (which is the 2nd smallest element)
