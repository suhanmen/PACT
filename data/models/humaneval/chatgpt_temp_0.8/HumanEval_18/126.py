def how_many_times(string: str, substring: str) -> int:
    count = 0
    start = 0
    while True:
        start = string.find(substring, start) # find the next occurrence of the substring
        if start == -1:
            break
        count += 1
        start += 1 # move start position to the right
    return count
