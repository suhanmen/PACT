def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    string = string.lower()  # convert all characters to lower case
    distinct_chars = set(string)  # get set of unique characters
    return len(distinct_chars)  # return the length of the set
