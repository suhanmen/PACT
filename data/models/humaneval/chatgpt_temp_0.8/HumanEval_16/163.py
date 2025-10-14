def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to make the comparison case-insensitive
    string = string.lower()
    # Create an empty set to store distinct characters
    distinct_chars = set()
    # Iterate through each character in the string and add it to the set if it hasn't been encountered before
    for char in string:
        if char not in distinct_chars:
            distinct_chars.add(char)
    # Return the size of the set, which represents the number of distinct characters in the string
    return len(distinct_chars)
