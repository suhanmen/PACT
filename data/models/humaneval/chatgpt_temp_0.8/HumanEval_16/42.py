python
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    # convert the string to lowercase to count distinct characters regardless of case
    string = string.lower()

    # create an empty set to keep track of distinct characters
    distinct_chars = set()

    # iterate over each character in the string
    for char in string:
        # add the character to the distinct_chars set if it has not been added already
        if char not in distinct_chars:
            distinct_chars.add(char)

    # return the length of the distinct_chars set
    return len(distinct_chars)
