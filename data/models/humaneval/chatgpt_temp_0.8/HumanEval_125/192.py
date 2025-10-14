def split_words(txt):
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        count = 0
        for letter in txt:
            if letter.islower():
                order = ord(letter) - ord('a')
                if order % 2 == 1:
                    count += 1
        return count
