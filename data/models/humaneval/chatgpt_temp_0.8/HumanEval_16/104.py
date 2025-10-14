def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lower case so that we can count case-insensitively
    string = string.lower()
    # Use a set to store the distinct characters
    distinct_chars = set()
    # Loop over each character in the string
    for char in string:
        # Add the character to the set
        distinct_chars.add(char)
    # Return the length of the set
    return len(distinct_chars)
