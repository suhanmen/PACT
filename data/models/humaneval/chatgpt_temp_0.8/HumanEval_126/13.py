def is_sorted(lst):
    if len(set(lst)) != len(lst):
        return False # list has more than 1 duplicate of the same number
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False # not in ascending order
    return True
