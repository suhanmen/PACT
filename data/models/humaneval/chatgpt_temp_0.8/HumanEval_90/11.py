def next_smallest(lst):
    if len(lst) < 2: # if the list doesn't have at least 2 elements, return None
        return None
    else:
        lst = sorted(set(lst)) # remove duplicates and sort the list
        if len(lst) >= 2:
            return lst[1] # return the 2nd smallest element
        else:
            return None # if there is no 2nd smallest element, return None
