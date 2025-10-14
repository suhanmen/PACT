def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    new_list = []
    for i, val in enumerate(l):
        if i % 3 == 0:
            sub_list = l[i:i+3]
            sorted_sub_list = sorted(sub_list)
            new_list += sorted_sub_list
        else:
            new_list.append(val)
    return new_list
