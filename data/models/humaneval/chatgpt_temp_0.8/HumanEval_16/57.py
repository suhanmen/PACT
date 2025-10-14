def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to treat uppercase and lowercase characters as the same
    string = string.lower()
    
    # Create an empty set to keep track of distinct characters
    distinct_chars = set()
    
    # Iterate over each character in the string and add it to the set
    for char in string:
        distinct_chars.add(char)
    
    # Return the size of the set, which represents the number of distinct characters
    return len(distinct_chars)
