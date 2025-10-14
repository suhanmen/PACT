def split_words(txt):
    # check if text contains whitespace
    if ' ' in txt:
        return txt.split()
    # check if text contains comma
    elif ',' in txt:
        return txt.split(',')
    else:
        # count the number of lowercase letters with odd alphabetical order
        count = 0
        for char in txt:
            if char.islower() and ord(char) % 2 != 0:
                count += 1
        return count
