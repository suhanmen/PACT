def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    even_indices = [i for i in range(len(l)) if i % 2 == 0] # get the even indices
    even_values = [l[i] for i in even_indices] # get the values at the even indices
    sorted_even_values = sorted(even_values) # sort the values
    result = [] # create an empty list to hold the result
    
    for i in range(len(l)):
        if i % 2 == 0: # if even index
            result.append(sorted_even_values.pop(0)) # append sorted value
        else:
            result.append(l[i]) # append original value
    
    return result
