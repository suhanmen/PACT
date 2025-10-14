def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indices, while its values at the even indices are equal
    to the values of the even indices of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    sorted_even_values = sorted([l[i] for i in even_indices])
    l_prime = l.copy()
    for i in even_indices:
        l_prime[i] = sorted_even_values.pop(0)
    return l_prime
