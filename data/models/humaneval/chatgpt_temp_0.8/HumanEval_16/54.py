def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # convert string to lowercase to remove case sensitivity
    string = string.lower()
    # create an empty set to store distinct characters
    distinct_chars = set()
    # iterate over each character in the string
    for char in string:
        # add the character to the set if it's not already there
        if char not in distinct_chars:
            distinct_chars.add(char)
    # return the number of distinct characters
    return len(distinct_chars)
