python
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to make the comparison case-insensitive
    string = string.lower()
    # Use a set to store unique characters in the string
    unique_chars = set()
    # Iterate over each character in the string
    for char in string:
        # If the character is not already in the set of unique characters, add it
        if char not in unique_chars:
            unique_chars.add(char)
    # Return the number of unique characters in the set
    return len(unique_chars)
