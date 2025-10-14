def split_words(txt):
    words = txt.split()
    if len(words) > 1:
        return words
    elif ',' in txt:
        return txt.split(',')
    else:
        odd_lower = len([c for c in txt if c.islower() and ord(c) % 2 == 1])
        return odd_lower
