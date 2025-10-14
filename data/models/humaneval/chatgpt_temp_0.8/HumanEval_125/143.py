def split_words(txt):
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        return sum([1 for letter in txt if letter.islower() and ord(letter) % 2 == 1])
