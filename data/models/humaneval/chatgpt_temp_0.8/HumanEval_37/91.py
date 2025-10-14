def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that l' is identical to l in the odd indices,
    while its values at the even indices are equal to the values of the even indices of l, but sorted.

    :param l: A list of integers
    :return: A list of integers with even indices sorted
    """
    even_indices = sorted([i for i in range(len(l)) if i % 2 == 0])
    even_values = [l[i] for i in even_indices]
    even_values.sort()
    result = l.copy()
    for i in range(len(even_indices)):
        result[even_indices[i]] = even_values[i]
    return result
