def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to ignore case
    string = string.lower()
    # Create an empty set to store distinct characters
    distinct_chars = set()
    # Iterate through each character in the string
    for char in string:
        # Check if the character is already in the set
        if char not in distinct_chars:
            # If not, add it to the set
            distinct_chars.add(char)
    # Return the size of the set, which is the number of distinct characters
    return len(distinct_chars)
