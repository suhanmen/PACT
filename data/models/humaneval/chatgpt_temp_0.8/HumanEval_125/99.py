def split_words(txt):
    # Split on whitespace if it exists
    if ' ' in txt:
        return txt.split()
    # Split on commas if no whitespaces exist
    elif ',' in txt:
        return txt.split(',')
    # Count odd-order lowercase letters if neither exist
    else:
        count = 0
        for char in txt:
            if char.islower() and ord(char)%2 != 0:
                count += 1
        return count
