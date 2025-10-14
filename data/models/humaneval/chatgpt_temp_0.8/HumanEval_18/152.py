def how_many_times(string: str, substring: str) -> int:
    count = 0
    start_index = 0
    while True:
        index = string.find(substring, start_index)
        if index == -1:
            break
        count += 1
        start_index = index + 1
    return count
