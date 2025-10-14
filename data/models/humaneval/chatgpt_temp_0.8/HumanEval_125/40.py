def split_words(txt):
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        count = 0
        for word in txt:
            for letter in word:
                if letter.islower():
                    if ord(letter) % 2 == 1:
                        count += 1
        return count
