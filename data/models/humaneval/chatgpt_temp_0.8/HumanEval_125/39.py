def split_words(txt):
    words = txt.split()
    if len(words) == 1:
        words = txt.split(',')
        if len(words) == 1:
            count = 0
            for c in txt:
                if c.islower():
                    if ord(c) % 2 == 1:
                        count += 1
            return count
    return words
