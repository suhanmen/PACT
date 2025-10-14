def how_many_times(string: str, substring: str) -> int:
    count = 0
    if substring == "":
        return 0
    while True:
        index = string.find(substring)
        if index == -1:
            break
        count += 1
        string = string[index + 1:]
    return count
