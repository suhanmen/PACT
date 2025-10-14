def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lower case to make it case-insensitive
    string = string.lower()
    
    # Use set to get the distinct characters in the string
    distinct_chars = set(string)
    
    # Return the length of the set
    return len(distinct_chars)
