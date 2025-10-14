def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # convert all characters to lowercase and remove duplicates
    distinct_chars = set(string.lower())
    # return the length of the set
    return len(distinct_chars)
