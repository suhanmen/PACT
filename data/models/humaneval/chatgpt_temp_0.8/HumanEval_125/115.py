def split_words(txt):
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        odd_chars = 0
        for char in txt:
            if char.islower() and ord(char) % 2 == 1:
                odd_chars += 1
        return odd_chars
