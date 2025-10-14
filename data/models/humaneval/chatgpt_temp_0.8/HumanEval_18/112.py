def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlapping cases.

    Args:
        string (str): The original string to search in
        substring (str): The string to search for

    Returns:
        int: The number of times the substring is found in the original string

    Examples:
        >>> how_many_times('', 'a')
        0
        >>> how_many_times('aaa', 'a')
        3
        >>> how_many_times('aaaa', 'aa')
        3
    """
    count = 0
    index = 0
    while True:
        index = string.find(substring, index)  # Find the next occurrence of the substring
        if index == -1:
            break  # No more occurrences, so exit the loop
        count += 1
        index += 1  # Move to the next position to start the next search

    return count
