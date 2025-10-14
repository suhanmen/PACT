def split_words(txt):
    words = txt.split()
    if len(words) > 1:
        return words
    else:
        words = txt.split(",")
        if len(words) > 1:
            return words
        else:
            count = sum([ord(c) % 2 for c in txt if c.islower()])
            return count
