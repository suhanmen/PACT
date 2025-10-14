def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    """
    count = 0
    if substring == "":
        return count
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            count += 1
    return count
