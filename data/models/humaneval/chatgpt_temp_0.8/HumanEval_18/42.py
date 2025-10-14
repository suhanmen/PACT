def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlapping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if not string or not substring: # if either string or substring is empty, return 0
        return 0
    count = 0
    start = 0
    while True:
        start = string.find(substring, start) # find the substring in the string starting from index start
        if start == -1: # if not found, break the loop
            break
        count += 1 # increment the count as substring is found
        start += 1 # move the start index to look for overlapping cases
    return count
