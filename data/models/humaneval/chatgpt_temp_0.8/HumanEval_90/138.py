def next_smallest(lst):
    if len(lst) < 2: # if list has less than 2 elements, return None
        return None
    else:
        sorted_lst = sorted(set(lst)) # remove duplicates and sort the list
        if len(sorted_lst) < 2: # if list has less than 2 unique elements, return None
            return None
        else:
            return sorted_lst[1] # return the second smallest element
