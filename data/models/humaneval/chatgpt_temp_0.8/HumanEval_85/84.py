def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..

    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    sum_even = 0
    for i in range(1, len(lst), 2):  # checking only odd indices
        if lst[i] % 2 == 0:  # checking if the element is even
            sum_even += lst[i]
    return sum_even
