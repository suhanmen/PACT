def split_words(txt):
    words = txt.split()
    if len(words) == 1: # check if no whitespaces exist in the text
        words = txt.split(",")
    if len(words) == 1: # check if no commas exist in the text
        count = 0
        for letter in txt:
            if letter.islower() and ord(letter) % 2 != 0:
                count += 1
        return count
    return words
