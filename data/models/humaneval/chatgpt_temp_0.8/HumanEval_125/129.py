def split_words(txt):
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        count = 0
        for i in txt:
            if i.islower() and ord(i) % 2 != 0:
                count += 1
        return count
