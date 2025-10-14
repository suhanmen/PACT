def split_words(txt):
    if " " in txt:
        # split on whitespace
        return txt.split()
    elif "," in txt:
        # split on commas
        return txt.split(",")
    else:
        # count number of lowercase letters with odd order in alphabet
        odd_count = 0
        for letter in txt:
            if letter.islower() and ord(letter) % 2 != 0:
                odd_count += 1
        return odd_count
