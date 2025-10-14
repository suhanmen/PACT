def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    indices = range(len(l))
    # Create a list with the sorted values at every third index
    sorted_third = sorted(l[i] for i in indices if i % 3 == 0)
    # Create a new list with the values from the original list and the sorted values at every third index
    new_l = [l[i] if i % 3 != 0 else sorted_third.pop(0) for i in indices]
    return new_l
