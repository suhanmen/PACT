def anti_shuffle(s):
    words = s.split()  # split the string into words
    ordered_words = []
    for word in words:
        ordered_word = ''.join(sorted(word))  # sort the characters in the word
        ordered_words.append(ordered_word)
    # join the ordered words with the original spaces and return the result
    return ' '.join(ordered_words)
