def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # First, convert the string to lowercase so that case is ignored
    string = string.lower()

    # Create an empty set to hold the distinct characters we encounter
    distinct_chars = set()

    # Iterate over each character in the string
    for char in string:
        # If this is the first time we've seen this character, add it to the set
        if char not in distinct_chars:
            distinct_chars.add(char)

    # Return the size of the set (the number of distinct characters)
    return len(distinct_chars)
