def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    string = string.lower() # convert all characters to lowercase to ignore case
    distinct_characters = set(string) # use a set to get distinct characters
    return len(distinct_characters)
