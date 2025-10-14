def split_words(txt):
    if ' ' in txt:  # check if the text contains whitespace
        return txt.split()  # split the text on whitespace and return the list of words
    elif ',' in txt:  # check if the text contains commas
        return txt.split(',')  # split the text on commas and return the list of words
    else:
        # count the number of lower-case letters with odd order in the alphabet
        return len([char for char in txt if char.islower() and ord(char) % 2 == 1])
