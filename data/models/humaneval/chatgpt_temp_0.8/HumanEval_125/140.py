def split_words(txt):
    words = txt.split()
    if len(words) == 1:
        words = txt.split(",")
    if len(words) == 1:
        num_odd_alpha = sum(1 for c in txt if c.islower() and ord(c) % 2 == 1)
        return num_odd_alpha
    return words
