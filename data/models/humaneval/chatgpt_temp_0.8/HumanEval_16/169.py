def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lower case to ignore case sensitivity
    string = string.lower()
    
    # Create an empty set to store distinct characters
    distinct_characters = set()
    
    # Iterate through the string, adding each distinct character to the set
    for character in string:
        distinct_characters.add(character)
    
    # Return the length of the set
    return len(distinct_characters)
