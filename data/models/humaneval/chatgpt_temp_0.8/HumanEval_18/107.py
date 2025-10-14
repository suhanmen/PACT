def how_many_times(string: str, substring: str) -> int:
    count = 0
    start = 0
    while True:
        start = string.find(substring, start)
        if start != -1:
            count += 1
            start += 1
        else:
            return count
