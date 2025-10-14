def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # convert the string to lowercase to ignore case
    string = string.lower()
    # create an empty set to hold distinct characters
    distinct_characters = set()
    # loop through each character in the string and add it to the set
    for char in string:
        distinct_characters.add(char)
    # return the size of the set (number of distinct characters)
    return len(distinct_characters)
