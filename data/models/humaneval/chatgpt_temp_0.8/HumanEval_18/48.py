def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    """
    if not string or not substring:
        return 0
    
    count = 0
    start = 0
    
    while True:
        start = string.find(substring, start)
        if start != -1:
            count += 1
            start += 1
        else:
            break
            
    return count
