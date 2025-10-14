def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to all lowercase to ignore case sensitivity
    string = string.lower()
    
    # Create an empty set to store unique characters
    unique_chars = set()
    
    # Iterate over the string and add each character to the set
    for char in string:
        unique_chars.add(char)
        
    # Return the length of the set to get the number of distinct characters
    return len(unique_chars)
