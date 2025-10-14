def split_words(txt):
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        count = 0
        for c in txt:
            if c.islower() and ord(c) % 2 == 1:
                count += 1
        return count
