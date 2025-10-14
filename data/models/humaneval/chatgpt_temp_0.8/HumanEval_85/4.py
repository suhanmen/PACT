def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..

    Args:
        lst: A non-empty list of integers.

    Returns:
        The sum of even elements that are at odd indices in lst.

    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    return sum([num for i, num in enumerate(lst) if i % 2 == 1 and num % 2 == 0])
