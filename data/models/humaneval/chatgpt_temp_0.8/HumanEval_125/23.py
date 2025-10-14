def split_words(txt):
    # Check if the text contains whitespace
    if ' ' in txt:
        # Split the text on whitespace and return the list
        return txt.split()
    # Check if the text contains commas
    elif ',' in txt:
        # Split the text on commas and return the list
        return txt.split(',')
    else:
        # Count the number of lowercase letters with odd order in the alphabet and return the count
        return sum(1 for c in txt if c.islower() and ord(c) % 2 != 0)
