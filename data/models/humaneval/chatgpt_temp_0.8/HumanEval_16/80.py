def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert string to lowercase to ignore case differences
    string = string.lower()
    # Use a set to keep track of unique characters
    unique_chars = set(string)
    # Return the size of the set
    return len(unique_chars)
