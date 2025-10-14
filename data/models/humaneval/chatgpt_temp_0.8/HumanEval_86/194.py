def anti_shuffle(s):
    # split the string into words
    words = s.split()

    # initialize an empty list to store the ordered words
    ordered_words = []

    # loop through each word and order the characters based on ascii value
    for word in words:
        ordered_word = ''.join(sorted(word, key=lambda x: ord(x)))
        ordered_words.append(ordered_word)

    # join the ordered words back into a sentence
    ordered_sentence = ' '.join(ordered_words)

    return ordered_sentence
