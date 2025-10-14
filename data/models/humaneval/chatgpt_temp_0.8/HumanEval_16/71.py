def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to count unique characters regardless of case
    string = string.lower()
    
    # Create an empty set to store unique characters
    unique_chars = set()
    
    # Loop through each character in the string
    for char in string:
        # Add the character to the set if it's not already there
        unique_chars.add(char)
    
    # Return the length of the unique characters set
    return len(unique_chars)
