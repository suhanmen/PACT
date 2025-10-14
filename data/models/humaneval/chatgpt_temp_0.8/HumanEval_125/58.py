def split_words(txt):
    # Split on whitespace if it exists
    if " " in txt:
        words = txt.split()
    # Split on commas if no whitespace exists
    elif "," in txt:
        words = txt.split(",")
    # Count lower-case letters with odd alphabetical order if neither whitespace nor commas exist
    else:
        words = [c for c in txt if c.islower() and ord(c) % 2 == 1]
        words = len(words)
    return words
