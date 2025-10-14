def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    # Initialize an empty string
    result = ""
    
    # Loop from 0 to n and add each number to the string with a space delimiter
    for i in range(n+1):
        result += str(i) + " "
    
    # Return the string with trailing whitespace removed
    return result.strip()
