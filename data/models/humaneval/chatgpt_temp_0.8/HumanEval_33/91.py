def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    sorted_indices = sorted([i for i in range(len(l)) if i % 3 == 0])
    sorted_values = [l[i] for i in sorted_indices]
    result = [l[i] if i % 3 != 0 else sorted_values.pop(0) for i in range(len(l))]
    return result
