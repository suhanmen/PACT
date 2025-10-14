def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    string = string.lower()  # convert to lower case
    distinct_chars = set()  # create an empty set
    for char in string:
        if char not in distinct_chars:
            distinct_chars.add(char)  # add to set if not already there
    return len(distinct_chars)  # return the size of the set
