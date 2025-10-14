python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    third_indices = range(0, len(l), 3)
    third_values = [l[i] for i in third_indices]
    sorted_third_values = sorted(third_values)
    result = [x for i, x in enumerate(l) if i not in third_indices]
    for i, val in zip(third_indices, sorted_third_values):
        result.insert(i, val)
    return result
