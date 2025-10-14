def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # convert the string to lowercase to make it case-insensitive
    string = string.lower()
    # create an empty set to store unique characters
    unique_chars = set()
    # iterate over each character in the string
    for char in string:
        # check if the character is already in the set
        if char not in unique_chars:
            # if not, add it to the set
            unique_chars.add(char)
    # return the number of unique characters in the set
    return len(unique_chars)
