def anti_shuffle(s):
    words = s.split()  # split string into individual words
    ordered_words = []
    for word in words:
        ordered_word = ''.join(sorted(word))  # sort characters in word based on ascii value
        ordered_words.append(ordered_word)
    return ' '.join(ordered_words)  # join the ordered words into a sentence, separated by space
