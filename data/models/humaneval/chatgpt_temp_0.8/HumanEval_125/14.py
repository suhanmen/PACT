def split_words(txt):
    words = txt.split()
    if len(words) == 1:  # If no whitespaces exist
        words = txt.split(",")
        if len(words) == 1:  # If no commas exist
            odd_count = sum(1 for c in txt if c.islower() and ord(c) % 2 == 1)
            return odd_count
    return words
