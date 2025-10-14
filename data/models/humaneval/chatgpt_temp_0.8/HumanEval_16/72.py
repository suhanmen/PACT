def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # convert the string to lowercase for case-insensitive comparison
    string = string.lower()
    # create a set of the characters in the string
    distinct_chars = set(string)
    # return the length of the set
    return len(distinct_chars)
