def split_words(txt):
    if " " in txt:
        words = txt.split()
    elif "," in txt:
        words = txt.split(",")
    else:
        words = [char for char in txt if char.islower() and ord(char) % 2 == 1]
        words = len(words)
    return words
