def next_smallest(lst):
    if len(lst) < 2: # if the list contains less than 2 elements, there is no 2nd smallest
        return None
    else:
        sorted_list = sorted(set(lst)) # sort the list and get rid of duplicates
        if len(sorted_list) < 2: # if there is only one unique element, there is no 2nd smallest
            return None
        else:
            return sorted_list[1] # return the 2nd smallest element
