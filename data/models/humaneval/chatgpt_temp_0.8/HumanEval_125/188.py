def split_words(txt):
    words = txt.split()
    if len(words) == 1:
        words = txt.split(",")
    if len(words) == 1:
        odd_letters = [char for char in txt if char.islower() and ord(char) % 2 != 0]
        return len(odd_letters)
    return words
