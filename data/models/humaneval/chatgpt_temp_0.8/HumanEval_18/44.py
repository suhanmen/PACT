def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlapping cases.
    """
    if not substring:
        return 0
    count = 0
    i = 0
    while True:
        i = string.find(substring, i)
        if i == -1:
            break
        count += 1
        i += 1
    return count
