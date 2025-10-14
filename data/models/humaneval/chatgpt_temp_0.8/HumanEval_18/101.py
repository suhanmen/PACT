def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlapping cases.
    """
    count = 0
    start = 0
    while True:
        start = string.find(substring, start)  # get the index of the substring
        if start == -1:  # if the substring is not found, exit the loop
            break
        count += 1
        start += 1  # move the starting index for the next search
    return count
