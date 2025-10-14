def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to ignore case
    string = string.lower()
    
    # Use a set to keep track of distinct characters
    distinct_chars = set()
    
    # Add each character to the set
    for char in string:
        distinct_chars.add(char)
    
    # Return the number of distinct characters in the set
    return len(distinct_chars)
