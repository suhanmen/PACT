def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    div_three = []
    other = []
    for i, x in enumerate(l):
        if i % 3 == 0:
            div_three.append(x)
        else:
            other.append(x)
    div_three.sort()
    result = []
    for i, x in enumerate(l):
        if i % 3 == 0:
            result.append(div_three.pop(0))
        else:
            result.append(other.pop(0))
    return result
