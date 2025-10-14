def split_words(txt):
    # split on whitespace if it exists
    if ' ' in txt:
        return txt.strip().split()
    # split on commas if no whitespace exists
    elif ',' in txt:
        return txt.strip().split(',')
    else:
        # count lowercase letters with odd order in alphabet
        count = 0
        for char in txt:
            if char.islower() and ord(char) % 2 == 1:
                count += 1
        return count
