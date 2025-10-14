def next_smallest(lst):
    if len(set(lst)) < 2: # if there are less than 2 unique elements in the list
        return None
    else:
        sorted_lst = sorted(set(lst)) # remove duplicates and sort the list
        return sorted_lst[1] # return the second smallest element
