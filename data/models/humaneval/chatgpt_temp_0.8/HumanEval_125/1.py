def split_words(txt):
    words = txt.split()
    if len(words) > 1:
        return words
    elif "," in txt:
        return txt.split(",")
    else:
        odd_count = 0
        for letter in txt:
            if letter.islower() and ord(letter) % 2 != 0:
                odd_count += 1
        return odd_count
