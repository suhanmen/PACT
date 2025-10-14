def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    # Create a list of numbers ranging from 0 to n inclusive
    numbers = list(range(n+1))
    # Join the numbers with a space delimiter and return the resulting string
    return " ".join(str(num) for num in numbers)
