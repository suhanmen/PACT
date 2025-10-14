def anti_shuffle(s):
    words = s.split()  # split the string into a list of words
    ordered_words = []  # create an empty list to store the ordered words
    for word in words:
        ordered_word = ''.join(sorted(word))  # sort the characters in the word based on ascii value
        ordered_words.append(ordered_word)  # add the ordered word to the list
    return ' '.join(ordered_words)  # join the ordered words with spaces and return the resulting string
