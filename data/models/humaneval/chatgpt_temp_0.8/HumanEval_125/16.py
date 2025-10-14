def split_words(txt):
    if ' ' in txt: # check if whitespace exists in the text
        return txt.split() # split words on whitespace
    elif ',' in txt: # check if comma exists in the text
        return txt.split(',') # split words on comma
    else:
        # count the number of lower-case letters with odd order in the alphabet
        # using a list comprehension and the ord() function
        count = len([char for char in txt if char.islower() and ord(char) % 2 == 1])
        return count
