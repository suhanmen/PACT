def split_words(txt):
    if " " in txt:
        # if there is whitespace, split on it and return the list of words
        return txt.split()
    elif "," in txt:
        # if there are no whitespaces but there are commas, split on commas and return the list of words
        return txt.split(",")
    else:
        # if there are no whitespaces or commas, count the number of lowercase letters with odd alphabetical order
        # (i.e. letters with an odd index in the alphabetical order)
        odd_letters_count = 0
        for letter in txt:
            if letter.islower() and ord(letter) % 2 != 0:
                odd_letters_count += 1
        return odd_letters_count
