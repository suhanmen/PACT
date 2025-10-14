def anti_shuffle(s):
    words = s.split() # split the string into words
    ordered_words = [] # initialize a list to hold the ordered words
    for word in words:
        ordered_word = "".join(sorted(word)) # sort the characters in each word in ascending ascii order
        ordered_words.append(ordered_word) # add the ordered word to the list
    return " ".join(ordered_words) # join the ordered words back into a string with spaces between them
