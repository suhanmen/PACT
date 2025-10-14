def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # convert all characters to lowercase to consider case-insensitivity
    string = string.lower()
    # create an empty set to store distinct characters
    distinct_chars = set()
    # loop through each character in the string
    for char in string:
        # if the character is not in the distinct_chars set, add it
        if char not in distinct_chars:
            distinct_chars.add(char)
    # return the length of the distinct_chars set
    return len(distinct_chars)
