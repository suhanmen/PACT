def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    string = string.lower() # convert string to lower case
    unique_chars = set(string) # create a set of unique characters
    return len(unique_chars) # return the length of the set
