def count_upper(s):
    count = 0
    vowels = 'AEIOU'
    for i in range(0, len(s), 2):
        if s[i] in vowels and s[i].isupper():
            count += 1
    return count
