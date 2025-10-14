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
    unique_characters = set()
    
    # iterate over the string, adding each character to the set
    for char in string:
        unique_characters.add(char)
        
    # return the length of the set
    return len(unique_characters)
