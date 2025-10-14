def split_words(txt):
    if ' ' in txt:  # split on whitespace if exists
        return txt.split()
    elif ',' in txt:  # split on commas if exists
        return txt.split(',')
    else:  # count number of lower-case letters with odd order in the alphabet
        count = 0
        for char in txt:
            if char.islower() and ord(char) % 2 != 0:
                count += 1
        return count
