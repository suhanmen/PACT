def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase and remove any whitespace
    string = string.lower().replace(" ", "")
    
    # Use a set to store the distinct characters
    distinct_chars = set(string)
    
    # Return the length of the set
    return len(distinct_chars)
