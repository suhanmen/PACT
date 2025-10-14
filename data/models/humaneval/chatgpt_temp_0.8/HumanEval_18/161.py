def how_many_times(string: str, substring: str) -> int:
    count = 0
    if not string or not substring:
        return count
    
    for i in range(len(string)):
        if string[i:].startswith(substring):
            count += 1
    return count
