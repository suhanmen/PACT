def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Create a set to store the distinct characters
    distinct_chars = set()
    
    # Convert the string to lowercase to ignore case
    string = string.lower()
    
    # Loop through each character in the string
    for char in string:
        # Add the character to the set if it's not already in there
        if char not in distinct_chars:
            distinct_chars.add(char)
    
    # Return the length of the set
    return len(distinct_chars)
