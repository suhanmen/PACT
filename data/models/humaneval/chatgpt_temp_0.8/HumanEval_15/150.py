def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    # initialize an empty string
    result = ''
    
    # loop through the range from 0 to n, inclusive
    for i in range(n+1):
        # add the current number to the result string, followed by a space
        result += str(i) + ' '
    
    # remove the extra space at the end of the string and return the result
    return result.strip()
