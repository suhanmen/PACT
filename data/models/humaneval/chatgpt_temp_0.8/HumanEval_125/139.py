def split_words(txt):
    # split on whitespace
    words = txt.split()
    if len(words) > 1:
        return words
    # split on commas
    words = txt.split(',')
    if len(words) > 1:
        return words
    # count odd letters if no whitespaces or commas
    count = 0
    for letter in txt:
        if letter.islower() and ord(letter) % 2 != 0:
            count += 1
    return count
