def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # convert string to lowercase to make it case-insensitive
    string = string.lower()
    # create a set of distinct characters in the string
    distinct_chars = set(string)
    # return the size of the set
    return len(distinct_chars)
