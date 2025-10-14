def next_smallest(lst):
    if len(lst) < 2:  # if the list has less than 2 elements
        return None  # there is no 2nd smallest element, so return None
    else:
        lst = list(set(lst))  # remove duplicates
        lst.sort()  # sort in ascending order
        if len(lst) < 2:  # if there is only 1 unique element in the list
            return None  # there is no 2nd smallest element, so return None
        else:
            return lst[1]  # return the 2nd smallest element
