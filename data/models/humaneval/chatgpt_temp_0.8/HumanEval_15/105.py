def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    # Create an empty list to store the numbers
    numbers = []
    # Loop through the numbers from 0 to n
    for i in range(n+1):
        # Add the number to the list
        numbers.append(str(i))
    # Join the numbers with spaces and return the string
    return ' '.join(numbers)
