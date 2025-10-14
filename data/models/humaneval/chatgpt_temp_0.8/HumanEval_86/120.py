def anti_shuffle(s):
    words = s.split() # split the string into words
    ordered_words = [] # create an empty list to store the ordered words
    for word in words:
        ordered_word = ''.join(sorted(word)) # sort the characters in the word and join them back into a string
        ordered_words.append(ordered_word) # add the ordered word to the list
    return ' '.join(ordered_words) # join the ordered words back into a string with spaces between them
