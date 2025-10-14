def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 up to n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    # Create a list of numbers from 0 up to n
    numbers = list(range(n+1))
    # Convert the list of numbers to a string with space delimiters
    numbers_str = ' '.join(map(str, numbers))
    return numbers_str
