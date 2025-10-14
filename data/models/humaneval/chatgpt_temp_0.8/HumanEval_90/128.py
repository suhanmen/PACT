def next_smallest(lst):
    if len(lst) < 2:  # if the list has less than 2 elements, return None
        return None
    sorted_lst = sorted(set(lst))  # remove duplicates and sort the list
    if len(sorted_lst) < 2:  # if there is only one unique element, return None
        return None
    return sorted_lst[1]  # return the second smallest element
