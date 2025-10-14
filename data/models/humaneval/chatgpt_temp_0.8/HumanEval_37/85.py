def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    even_values = sorted(l[::2]) # Get even indices and sort them
    l_prime = [0] * len(l) # create a new list to hold sorted values
    for i in range(len(l)):
        if i % 2 == 0:
            l_prime[i] = even_values.pop(0) # add sorted even value to new list
        else:
            l_prime[i] = l[i] # add odd value to new list
    return l_prime
