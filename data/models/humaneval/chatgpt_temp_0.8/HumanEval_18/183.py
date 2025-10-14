def how_many_times(string: str, substring: str) -> int:
    count = 0
    start = 0
    while True:
        start = string.find(substring, start) + 1
        if start > 0:
            count += 1
        else:
            return count
