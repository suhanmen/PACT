def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    even_indices = l[::2]  # get even indices
    even_sorted = sorted(even_indices)  # sort even indices
    odd_indices = l[1::2]  # get odd indices
    result = [None] * (len(even_sorted) + len(odd_indices))  # initialize result list
    result[::2] = even_sorted  # place sorted even numbers
    result[1::2] = odd_indices  # place odd numbers
    return result
