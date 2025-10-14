def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # extract even indexed elements
    even_elements = l[::2]
    # sort even indexed elements
    even_elements.sort()
    # create new list with even indexed elements sorted and odd indexed elements unaltered
    new_list = [l[i] if i % 2 != 0 else even_elements[i//2] for i in range(len(l))]
    return new_list
