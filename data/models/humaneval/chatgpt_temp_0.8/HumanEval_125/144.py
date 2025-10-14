def split_words(txt):
    words = txt.split()
    if len(words) == 1 and ',' in txt:
        words = txt.split(',')
    if len(words) == 1:
        count = sum([1 for c in txt if c.islower() and ord(c) % 2 == 1])
        return count
    return words
