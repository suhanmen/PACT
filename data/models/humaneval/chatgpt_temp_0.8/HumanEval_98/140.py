def count_upper(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    count = 0
    for i in range(0, len(s), 2):
        if s[i].upper() in vowels:
            count += 1
    return count
