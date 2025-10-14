def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    """
    count = 0
    start = 0
    while True:
        start = string.find(substring, start) # Find the next occurrence of the substring
        if start == -1:
            break # If no more occurrence found, break out of the while loop
        count += 1
        start += 1 # Set the start to the next position after the current occurrence
    return count
