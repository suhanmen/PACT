def anti_shuffle(s):
    # Split the string into words
    words = s.split()

    # Create an empty list to hold the ordered words
    ordered_words = []

    # For each word, sort the characters based on their ascii value
    # and append the ordered word to the ordered_words list
    for word in words:
        ordered_word = ''.join(sorted(word))
        ordered_words.append(ordered_word)

    # Join the ordered words into a string, separated by spaces
    ordered_string = ' '.join(ordered_words)

    return ordered_string
