def split_words(txt):
    words = txt.split()
    if len(words) > 1:
        return words
    else:
        words = txt.split(',')
        if len(words) > 1:
            return words
        else:
            odd_letters = [letter for letter in txt if letter.islower() and ord(letter) % 2 == 1]
            return len(odd_letters)
