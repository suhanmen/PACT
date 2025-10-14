def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indices, while its values at the even indices are equal
    to the values of the even indices of l, but sorted.
    """
    even_values = sorted([l[i] for i in range(0, len(l), 2)])
    result = [l[i] if i % 2 != 0 else even_values.pop(0) for i in range(len(l))]
    return result
