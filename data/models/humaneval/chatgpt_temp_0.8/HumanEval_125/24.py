def split_words(txt):
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        count = 0
        for word in txt:
            if word.islower() and ord(word) % 2 == 1:
                count += 1
        return count
