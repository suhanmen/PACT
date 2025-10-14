def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlapping cases.
    """
    if not string or not substring:  # if either of the strings is empty return 0
        return 0
    count = 0
    start = 0
    while True:
        start = string.find(substring, start)  # find the substring in the string starting from the last found index
        if start == -1:  # if the substring is not found
            break
        count += 1
        start += 1  # move start to the next index
    return count
