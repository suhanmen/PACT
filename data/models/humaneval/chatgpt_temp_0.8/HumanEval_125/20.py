def split_words(txt):
    words = txt.split()
    if len(words) > 1:
        return words
    elif ',' in txt:
        return txt.split(',')
    else:
        count = 0
        for char in txt:
            if char.islower() and ord(char) % 2 != 0:
                count += 1
        return count
