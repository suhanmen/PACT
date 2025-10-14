def add(lst):
    """Given a non-empty list of integers lst, add the even elements that are at odd indices."""
    sum = 0
    for i in range(1, len(lst), 2):  # iterate over odd indices
        if lst[i] % 2 == 0:  # check if element at odd index is even
            sum += lst[i]  # add it to the sum
    return sum
