def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to ignore case differences
    string = string.lower()
    # Create an empty list to store the distinct characters from the string
    distinct_chars = []
    # Iterate through each character in the string
    for char in string:
        # If the character is not already in the distinct_chars list, add it
        if char not in distinct_chars:
            distinct_chars.append(char)
    # Return the length of the distinct_chars list
    return len(distinct_chars)
