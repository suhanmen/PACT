def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to make the comparisons case-insensitive
    string = string.lower()
    
    # Use a set to keep track of the distinct characters in the string
    distinct_characters = set()
    
    # Loop through each character in the string and add it to the set
    for char in string:
        distinct_characters.add(char)
    
    # Return the number of distinct characters in the set
    return len(distinct_characters)
