python
def split_words(txt):
    # Check if there are any whitespaces in the text
    if ' ' in txt:
        # Split on whitespace
        words = txt.split()
    # Check if there are any commas in the text
    elif ',' in txt:
        # Split on commas
        words = txt.split(',')
    else:
        # Count the number of lowercase letters with odd order in the alphabet
        words = [c for c in txt if c.islower() and ord(c) % 2 == 1]
        return len(words)
    return words
