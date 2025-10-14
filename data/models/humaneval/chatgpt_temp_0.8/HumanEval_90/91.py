def next_smallest(lst):
    if len(lst) < 2 or len(set(lst)) < 2: # if the list has less than 2 elements or only 1 distinct element
        return None
    else:
        sorted_lst = sorted(set(lst)) # remove duplicates and sort the list
        return sorted_lst[1] # return the second element, which is the 2nd smallest element
