def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert string to lowercase for case-insensitive comparison
    string = string.lower()
    # Use a set to store distinct characters
    distinct_chars = set()
    # Iterate through each character in the string
    for char in string:
        # If character is not already in the set, add it
        if char not in distinct_chars:
            distinct_chars.add(char)
    # Return the size of the set as the number of distinct characters
    return len(distinct_chars)
