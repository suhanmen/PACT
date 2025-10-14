def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the input string to lowercase
    string = string.lower()

    # Create an empty set to store the distinct characters
    distinct_characters = set()

    # Loop through each character in the string and add to the set if it is not already there
    for character in string:
        if character not in distinct_characters:
            distinct_characters.add(character)

    # Return the length of the set
    return len(distinct_characters)
