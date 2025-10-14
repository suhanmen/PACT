def next_smallest(lst):
    if len(lst) < 2: # if the list is empty or has only 1 element, there is no 2nd smallest element
        return None
    lst = sorted(set(lst)) # remove duplicates and sort the list in ascending order
    if len(lst) < 2: # if the list has only 1 unique element, there is no 2nd smallest element
        return None
    return lst[1] # return the 2nd element in the sorted list, which is the 2nd smallest
