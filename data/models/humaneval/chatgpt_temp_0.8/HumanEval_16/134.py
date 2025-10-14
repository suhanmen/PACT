def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # convert the string to lowercase
    string = string.lower()
    
    # create an empty set to keep track of unique characters
    unique_chars = set()
    
    # loop through each character in the string
    for char in string:
        # if the character is not already in the set, add it
        if char not in unique_chars:
            unique_chars.add(char)
    
    # return the number of unique characters
    return len(unique_chars)
