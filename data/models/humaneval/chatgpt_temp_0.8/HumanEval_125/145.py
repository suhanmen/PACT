def split_words(txt):
    words = txt.split()
    if len(words) > 1:
        return words
    else:
        words = txt.split(",")
        if len(words) > 1:
            return words
        else:
            count = 0
            for letter in txt:
                if letter.islower() and ord(letter) % 2 == 1:
                    count += 1
            return count
