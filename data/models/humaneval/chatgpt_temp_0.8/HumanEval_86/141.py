def anti_shuffle(s):
    words = s.split()  # split the string into a list of words
    ordered_words = []  # create an empty list to store the ordered words

    for word in words:
        ordered_word = ''.join(sorted(word))  # sort the characters in the word
        ordered_words.append(ordered_word)  # add the ordered word to the list

    # join the ordered words back into a string, preserving whitespace
    ordered_string = ' '.join(ordered_words)
    return ordered_string
