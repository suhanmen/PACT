def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indices, while its values at the even indices are equal
    to the values of the even indices of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    even_nums = sorted([num for num in l if l.index(num) % 2 == 0])
    return [even_nums.pop(0) if i % 2 == 0 else l[i] for i in range(len(l))]
