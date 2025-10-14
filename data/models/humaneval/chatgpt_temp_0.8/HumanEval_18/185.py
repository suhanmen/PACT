def how_many_times(string: str, substring: str) -> int:
    count = 0
    start = 0
    while True:
        start = string.find(substring, start) # get the index of the first occurrence of the substring
        if start == -1: # if the substring is not found, break the loop
            break
        count += 1
        start += 1 # start searching for the next occurrence of the substring after the current position
    return count
