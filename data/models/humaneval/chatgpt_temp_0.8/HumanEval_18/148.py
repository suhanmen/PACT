def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlapping cases.
    """
    if not substring:
        return 0
    count = 0
    index = 0
    while True:
        index = string.find(substring, index) + 1
        if index > 0:
            count += 1
        else:
            return count
