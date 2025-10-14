def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that l' is identical to l in the odd indicies,
    while its values at the even indicies are equal to the values of the even indicies of l, but sorted.
    """
    even_indices = [i for i in range(len(l)) if i % 2 == 0] # get the even indices
    even_vals_sorted = sorted([l[i] for i in even_indices]) # get the even values sorted
    l_prime = l[:] # make a copy of l
    # replace the even indices of l' with the sorted even values
    for i in even_indices:
        l_prime[i] = even_vals_sorted.pop(0)
    return l_prime
