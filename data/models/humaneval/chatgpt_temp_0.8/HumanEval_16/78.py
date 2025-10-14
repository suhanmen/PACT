def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert string to all lowercase
    string = string.lower()
    
    # Create a set to store distinct characters
    distinct_chars = set()
    
    # Iterate through each character in the string
    for char in string:
        # Add the character to the set if it's not already present
        if char not in distinct_chars:
            distinct_chars.add(char)
    
    # Return the length of the set, which represents the number of distinct characters
    return len(distinct_chars)
