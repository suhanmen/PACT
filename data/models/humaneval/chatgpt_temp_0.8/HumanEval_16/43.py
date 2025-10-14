def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # convert the string to lowercase to make it case-insensitive
    string = string.lower()
    
    # create an empty set to hold the distinct characters
    distinct_chars = set()
    
    # iterate over each character in the string and add it to the set if it doesn't already exist
    for char in string:
        if char not in distinct_chars:
            distinct_chars.add(char)
    
    # return the number of distinct characters in the set
    return len(distinct_chars)
