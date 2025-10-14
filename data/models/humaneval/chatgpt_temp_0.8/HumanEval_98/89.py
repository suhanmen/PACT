def count_upper(s):
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in 'AEIOU' and s[i].isupper():
            count += 1
    return count
