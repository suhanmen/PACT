def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert string to lowercase to make it case-insensitive
    string = string.lower()
    # Create an empty set to keep track of distinct characters
    distinct_chars = set()
    # Iterate over each character in the string
    for char in string:
        # Add the character to the set if it's not already there
        if char not in distinct_chars:
            distinct_chars.add(char)
    # Return the size of the set, which gives the number of distinct characters
    return len(distinct_chars)
