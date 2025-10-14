def next_smallest(lst):
    if len(lst) < 2 or len(set(lst)) < 2:
        return None  # if there are less than 2 unique elements, return None
    else:
        lst.sort()
        return lst[1]  # return the second element after sorting the list
