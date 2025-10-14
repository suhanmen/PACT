def split_words(txt):
    words = txt.split()
    if len(words) > 1:
        return words
    elif ',' in txt:
        return txt.split(',')
    else:
        return sum([1 for letter in txt if letter.islower() and ord(letter) % 2 == 1])
