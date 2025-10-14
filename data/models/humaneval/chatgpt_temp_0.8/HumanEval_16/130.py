def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase
    string = string.lower()
    # Use a set to store the distinct characters
    distinct_chars = set()
    # Iterate over each character in the string
    for char in string:
        # Check if the character is a letter
        if char.isalpha():
            # Add the lowercase character to the set
            distinct_chars.add(char)
    # Return the number of distinct characters
    return len(distinct_chars)
