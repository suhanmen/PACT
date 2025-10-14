def how_many_times(string: str, substring: str) -> int:
    count = 0
    if not string or not substring:
        return count
    i = 0
    while i < len(string):
        if string[i:].startswith(substring):
            count += 1
        i += 1
    return count
