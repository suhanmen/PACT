def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..
    
    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    total = 0
    for i in range(1, len(lst), 2):  # iterate over odd indices
        if lst[i] % 2 == 0:  # check if element is even
            total += lst[i]  # add to total if even
    return total
