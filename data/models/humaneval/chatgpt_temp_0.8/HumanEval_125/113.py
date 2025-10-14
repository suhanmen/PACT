def split_words(txt):
    words = txt.split()
    if len(words) == 1:
        words = txt.split(',')
        if len(words) == 1:
            count = sum(1 for c in txt if c.islower() and ord(c) % 2 != 0)
            return count
    return words
