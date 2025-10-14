def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    # Start with an empty string
    seq_str = ""

    # Loop through the numbers from 0 to n
    for i in range(n+1):
        # Add the number to the string with a space after it
        seq_str += str(i) + " "

    # Strip the trailing space and return the string
    return seq_str.strip()
