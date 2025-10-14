def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of
    """
    # convert the string to lower case and convert it to a set to get distinct characters
    distinct_chars = set(string.lower())

    # return the length of the set
    return len(distinct_chars)
