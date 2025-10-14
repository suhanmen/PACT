def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    """
    count = 0
    start = 0
    while True:
        start = string.find(substring, start) # find the next occurrence of substring
        if start == -1: # if substring not found, break the loop
            break
        count += 1 # increment the count
        start += 1 # start searching from the next index
    return count
