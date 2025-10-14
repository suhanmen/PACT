def split_words(txt):
    words = txt.split()
    if len(words) > 1:
        return words
    words = txt.split(',')
    if len(words) > 1:
        return words
    count = 0
    for c in txt:
        if c.islower() and ord(c) % 2 == 1:
            count += 1
    return count
