def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    """
    if not string or not substring or len(substring) > len(string):
        return 0
    count = 0
    start_index = 0
    while True:
        index = string.find(substring, start_index)
        if index == -1:
            break
        count += 1
        start_index = index + 1
    return count
