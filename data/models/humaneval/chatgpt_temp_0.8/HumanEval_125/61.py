def split_words(txt):
    words = txt.split()
    if len(words) == 1:
        words = txt.split(',')
        if len(words) == 1:
            count = len([ch for ch in txt if ch.islower() and ord(ch) % 2 != 0])
            return count if count != 0 else None
    return words
