def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlapping cases."""
    # Initialize a count variable
    count = 0
    # Loop over the string with a step size of 1
    for i in range(len(string) - len(substring) + 1):
        # Check if the substring appears at the current position
        if string[i:i+len(substring)] == substring:
            count += 1
    return count
