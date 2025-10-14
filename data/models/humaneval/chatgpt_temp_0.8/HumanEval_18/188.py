def how_many_times(string: str, substring: str) -> int:
    count = 0
    if len(string) == 0 or len(substring) == 0:
        return count
    else:
        index = 0
        while True:
            index = string.find(substring, index)
            if index != -1:
                count += 1
                index += 1
            else:
                break
    return count
