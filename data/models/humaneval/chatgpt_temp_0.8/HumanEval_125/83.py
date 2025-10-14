def split_words(txt):
    words = txt.split()
    if len(words) == 1: # if no whitespace, split on commas
        words = txt.split(",")
    if len(words) == 1: # if no commas, count lower-case letters with odd order in the alphabet
        count = 0
        for letter in txt:
            if letter.islower() and ord(letter) % 2 == 1:
                count += 1
        return count
    return words
