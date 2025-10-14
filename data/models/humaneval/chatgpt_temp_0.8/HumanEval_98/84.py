def count_upper(s):
    count = 0
    vowels = "AEIOU"
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in vowels:
            count += 1
    return count
