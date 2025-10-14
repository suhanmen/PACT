def anti_shuffle(s):
    # Split the string into a list of words
    words = s.split()

    # Create a list of ordered words
    ordered_words = []
    for word in words:
        ordered_word = ''.join(sorted(word))
        ordered_words.append(ordered_word)

    # Combine the ordered words into a single string
    ordered_string = ' '.join(ordered_words)

    return ordered_string
