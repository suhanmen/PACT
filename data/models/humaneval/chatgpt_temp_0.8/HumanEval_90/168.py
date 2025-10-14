def next_smallest(lst):
    if len(set(lst)) < 2:  # if there are less than 2 unique values in the list
        return None
    else:
        return sorted(set(lst))[1]  # sort the unique values in ascending order and return the second element
