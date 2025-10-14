def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # create a set to hold distinct characters
    distinct_chars = set()
    
    # loop through each character in the string
    for char in string:
        # convert the character to lowercase to ignore case
        char = char.lower()
        # add the character to the set if it doesn't already exist
        if char not in distinct_chars:
            distinct_chars.add(char)
    
    # return the size of the set, which is the count of distinct characters
    return len(distinct_chars)
