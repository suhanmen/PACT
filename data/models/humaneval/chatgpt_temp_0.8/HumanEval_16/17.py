def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert all characters to lowercase
    lower_string = string.lower()
    # Create a set of all unique characters
    unique_chars = set(lower_string)
    # Return the length of the set
    return len(unique_chars)
