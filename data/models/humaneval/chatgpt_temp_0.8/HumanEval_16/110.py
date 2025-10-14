def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # First, convert the string to lowercase to ignore case
    string = string.lower()
    # Then, use a set to store the distinct characters in the string
    distinct_chars = set(string)
    # Finally, return the length of the set
    return len(distinct_chars)
