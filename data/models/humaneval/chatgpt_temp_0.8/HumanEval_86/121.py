def anti_shuffle(s):
    words = s.split()  # split the input string into words
    ordered_words = []
    for word in words:
        # sort the characters in each word based on ascii value
        ordered_word = ''.join(sorted(word, key=lambda x: ord(x)))
        ordered_words.append(ordered_word)
    # join the ordered words back together with the original spaces
    return ' '.join(ordered_words)
