def anti_shuffle(s):
    words = s.split()  # split the string into words
    ordered_words = []
    for word in words:
        ordered_word = ''.join(sorted(word))  # sort the characters of the word
        ordered_words.append(ordered_word)
    # combine the ordered words back into a string with spaces
    ordered_string = ' '.join(ordered_words)
    return ordered_string
