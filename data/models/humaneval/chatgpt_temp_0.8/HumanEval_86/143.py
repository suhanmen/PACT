def anti_shuffle(s):
    words = s.split()  # split the words in the string
    new_words = []  # empty list to store new ordered words
    for word in words:
        ordered_word = ''.join(sorted(word))  # sort the characters in ascending order based on ascii value
        new_words.append(ordered_word)  # add the new ordered word to the list
    ordered_string = ' '.join(new_words)  # join the new ordered words with space
    return ordered_string
