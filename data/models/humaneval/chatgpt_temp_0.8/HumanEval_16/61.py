def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to ignore case sensitivity
    string = string.lower()
    
    # Use a set to store unique characters
    distinct_chars = set()
    
    # Loop through the characters in the string
    for char in string:
        # If the character is not already in the set, add it
        if char not in distinct_chars:
            distinct_chars.add(char)
    
    # Return the number of distinct characters in the set
    return len(distinct_chars)
