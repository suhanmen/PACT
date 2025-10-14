def split_words(txt):
    # Check if the text contains any whitespaces
    if ' ' in txt:
        return txt.split()
    # Check if the text contains any commas
    elif ',' in txt:
        return txt.split(',')
    else:
        # Count the number of lowercase letters with odd order in the alphabet
        count = 0
        for char in txt:
            if char.islower() and ord(char) % 2 == 1:
                count += 1
        return count
