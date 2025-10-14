def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    even_values = sorted(l[::2])
    odd_values = l[1::2]
    sorted_even_list = [None]*(len(even_values) + len(odd_values))
    sorted_even_list[::2] = even_values
    sorted_even_list[1::2] = odd_values
    return sorted_even_list
