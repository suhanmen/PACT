def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to ignore case sensitivity
    string = string.lower()
    # Create an empty set to store distinct characters
    distinct_chars = set()
    # Iterate over each character in the string
    for char in string:
        # Check if the character is not already in the set
        if char not in distinct_chars:
            # If the character is distinct, add it to the set
            distinct_chars.add(char)
    # Return the length of the set
    return len(distinct_chars)
