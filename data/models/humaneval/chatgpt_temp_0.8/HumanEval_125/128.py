def split_words(txt):
    # Split on whitespace if exists
    if ' ' in txt:
        return txt.split()
    # Split on commas if no white space exists
    elif ',' in txt:
        return txt.split(',')
    # Count lowercase letters with odd ord values if no commas or spaces exist
    else:
        return sum(1 for letter in txt if letter.islower() and ord(letter) % 2 != 0)
