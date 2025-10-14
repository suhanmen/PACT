def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # convert the string to lowercase
    string = string.lower()
    
    # create an empty set to hold unique characters
    unique_chars = set()
    
    # loop through each character in the string
    for char in string:
        # add the character to the unique_chars set
        unique_chars.add(char)
    
    # return the length of the unique_chars set
    return len(unique_chars)
