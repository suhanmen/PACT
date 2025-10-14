def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # First, convert the string to lowercase to ignore case differences
    string = string.lower()
    
    # Create an empty set to store the distinct characters
    distinct_chars = set()
    
    # Loop through each character in the string
    for char in string:
        # If the character is not already in the set of distinct characters, add it to the set
        if char not in distinct_chars:
            distinct_chars.add(char)
    
    # Return the size of the set of distinct characters
    return len(distinct_chars)
