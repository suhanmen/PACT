def count_distinct_characters(string: str) -> int:
    """Given a string, find out how many distinct characters (regardless of case) does it consist of"""
    # Convert all characters to lowercase for case-insensitivity
    string = string.lower()
    # Use set() to remove duplicates
    distinct_chars = set(string)
    # Return the length of the set
    return len(distinct_chars)
