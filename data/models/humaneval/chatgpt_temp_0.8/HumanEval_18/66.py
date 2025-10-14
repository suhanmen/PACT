def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    """
    if not string or not substring:
        return 0
        
    # Initialize count and start to 0
    count = 0
    start = 0
 
    # Search through the string till
    # we reach the end of it
    while start < len(string):
 
        # Check if a substring is present from
        # 'start' position till the end
        pos = string.find(substring, start)
 
        if pos != -1:
            # If a substring is present, move the
            # start to the next position from start
            start = pos + 1
 
            # Increment the count
            count += 1
        else:
            # If no further substring is present
            break
    return count
