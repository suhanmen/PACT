def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert string to lowercase to avoid case sensitivity
    string = string.lower()
    
    # Using set() to remove duplicates and len() to count the number of distinct characters
    return len(set(string))
