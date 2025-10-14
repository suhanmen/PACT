def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to avoid case sensitivity
    string = string.lower()

    # Create an empty set to store distinct characters
    distinct_chars = set()

    # Loop through all characters in the string and add them to the set
    for char in string:
        distinct_chars.add(char)

    # Return the length of the set
    return len(distinct_chars)
