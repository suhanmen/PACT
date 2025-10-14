def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # convert the string to lowercase to avoid case sensitivity
    string = string.lower()
    # use a set to store unique characters
    unique_chars = set()
    # loop through each character in the string and add it to the set
    for char in string:
        unique_chars.add(char)
    # return the length of the set
    return len(unique_chars)
