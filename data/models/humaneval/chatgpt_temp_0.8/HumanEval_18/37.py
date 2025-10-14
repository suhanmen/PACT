def how_many_times(string: str, substring: str) -> int:
    count = 0
    sub_len = len(substring)
    for i in range(len(string)-sub_len+1):
        if string[i:i+sub_len] == substring:
            count += 1
    return count
