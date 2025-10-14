def next_smallest(lst):
    if len(lst) < 2:
        return None
    else:
        lst = list(set(lst)) # remove duplicates
        lst.sort() # sort the list
        if len(lst) < 2:
            return None
        else:
            return lst[1] # return second smallest element
