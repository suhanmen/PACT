def split_words(txt):
    """
    Given a string of words, return a list of words split on whitespace,
    if no whitespaces exist in the text you should split on commas ','
    if no commas exist you should return the number of lowercase letters
    with an odd order in the alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    """
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        count = 0
        for char in txt:
            if char.islower() and ord(char) % 2 == 1:
                count += 1
        return count
