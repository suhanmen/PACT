def split_words(txt):
    if ' ' in txt:
        # Split on whitespace
        return txt.split()
    elif ',' in txt:
        # Split on commas
        return txt.split(',')
    else:
        # Count lowercase letters with odd order in the alphabet
        count = 0
        for char in txt:
            if char.islower() and ord(char) % 2 == 1:
                count += 1
        return count
