def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    string = string.lower() # Convert to lowercase
    distinct_chars = set(string) # Convert to set to remove duplicates
    return len(distinct_chars) # Return the length of the set
