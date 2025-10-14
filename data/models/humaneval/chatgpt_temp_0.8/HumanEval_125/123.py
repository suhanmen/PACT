def split_words(txt):
    words = txt.split()
    if len(words) == 1 and "," in txt:
        words = txt.split(",")
    elif len(words) == 1:
        count = 0
        for char in txt.lower():
            if char.isalpha() and ord(char) % 2 == 1:
                count += 1
        return count
    return words
