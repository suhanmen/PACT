def split_words(txt):
    words = txt.split()
    if len(words) > 1:
        return words
    elif "," in txt:
        return txt.split(",")
    else:
        return len([char for char in txt if char.islower() and ord(char) % 2 == 1])
