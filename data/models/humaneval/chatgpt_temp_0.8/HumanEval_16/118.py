def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to treat uppercase and lowercase characters as the same
    string = string.lower()
    
    # Create a set of unique characters in the string
    unique_chars = set(string)
    
    # Return the length of the set
    return len(unique_chars)
