def count_upper(s):
    count = 0
    for i in range(0, len(s), 2):
        if s[i].upper() in ['A', 'E', 'I', 'O', 'U']:
            count += 1
    return count
