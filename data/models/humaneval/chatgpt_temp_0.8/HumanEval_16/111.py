def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # convert the string to lowercase to ignore case distinctions
    string = string.lower()
    
    # initialize an empty set to keep track of the distinct characters
    distinct_chars = set()
    
    # loop through each character in the string
    for char in string:
        # add the character to the set if it hasn't been seen before
        distinct_chars.add(char)
    
    # return the number of distinct characters
    return len(distinct_chars)
