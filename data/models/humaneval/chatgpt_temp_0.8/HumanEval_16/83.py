def count_distinct_characters(string: str) -> int:
    """Given a string, find out how many distinct characters (regardless of case) does it consist of"""
    distinct_chars = set(string.lower()) # convert to lowercase and create a set of distinct characters
    return len(distinct_chars) # return the length of the set
