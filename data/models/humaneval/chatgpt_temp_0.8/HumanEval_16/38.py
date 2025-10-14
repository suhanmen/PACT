def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # convert the string to lower case
    string = string.lower()
    # create an empty set to store unique characters
    unique_chars = set()
    # iterate over each character in the string
    for char in string:
        # add the character to the set if it is not already in it
        if char not in unique_chars:
            unique_chars.add(char)
    # return the number of unique characters
    return len(unique_chars)
