def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlapping cases.
    """
    if not string or not substring:
        return 0
        
    count = 0
    i = 0
    while i < len(string) - len(substring) + 1:
        if string[i:i+len(substring)] == substring:
            count += 1
            i += 1
        else:
            i += 1
    return count
