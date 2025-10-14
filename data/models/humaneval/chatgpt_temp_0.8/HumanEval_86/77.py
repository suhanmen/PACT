def anti_shuffle(s):
    words = s.split()  # split the string into a list of words
    ordered_words = []

    for word in words:
        ordered_word = ''.join(sorted(word))  # sort the characters in the word
        ordered_words.append(ordered_word)

    # join the ordered words with their original whitespace
    ordered_string = ' '.join(ordered_words)
    return ordered_string
