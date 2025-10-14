def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..

    Args:
        lst: a non-empty list of integers

    Returns:
        sum of even elements that are at odd indices of the input list

    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    return sum([num for index, num in enumerate(lst) if index % 2 == 1 and num % 2 == 0])
