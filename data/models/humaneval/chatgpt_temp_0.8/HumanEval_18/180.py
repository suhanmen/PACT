def how_many_times(string: str, substring: str) -> int:
    if not string or not substring:
        return 0
    count = 0
    start = 0
    while True:
        index = string.find(substring, start)
        if index == -1:
            break
        count += 1
        start = index + 1
    return count
