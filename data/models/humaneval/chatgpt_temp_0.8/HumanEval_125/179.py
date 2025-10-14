def split_words(txt):
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        odd_count = sum([1 for letter in txt if ord(letter) % 2 == 1])
        return odd_count
