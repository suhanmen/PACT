def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert input string to lowercase
    string = string.lower()

    # Create a set of distinct characters in the string
    distinct_chars = set(string)

    # Count the number of distinct characters
    num_distinct_chars = len(distinct_chars)

    return num_distinct_chars
