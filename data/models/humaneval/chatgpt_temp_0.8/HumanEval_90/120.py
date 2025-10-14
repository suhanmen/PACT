def next_smallest(lst):
    if len(lst) < 2: # if the list has less than 2 elements
        return None # there is no 2nd smallest element
    smallest = min(lst) # find the smallest element
    lst.remove(smallest) # remove it from the list
    second_smallest = min(lst) # find the new smallest element
    if smallest == second_smallest: # if the smallest element was repeated
        return None # there is no 2nd smallest element
    else:
        return second_smallest # return the 2nd smallest element
