def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # convert the string to lowercase to ignore case
    string = string.lower()
    # use a set to store unique characters in the string
    unique_chars = set(string)
    # return the length of the set as the number of distinct characters
    return len(unique_chars)
