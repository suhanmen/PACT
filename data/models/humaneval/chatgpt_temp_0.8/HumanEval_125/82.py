def split_words(txt):
    # Check if the text contains any whitespace
    if ' ' in txt:
        # Split the text on whitespace and return the list of words
        return txt.split()
    # If there are no whitespaces, check if the text contains any commas
    elif ',' in txt:
        # Split the text on commas and return the list of words
        return txt.split(',')
    else:
        # Count the number of lower-case letters with odd order in the alphabet
        count = sum(1 for c in txt if c.islower() and ord(c) % 2 == 1)
        return count
