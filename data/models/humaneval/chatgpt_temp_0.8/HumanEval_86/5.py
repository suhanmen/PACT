def anti_shuffle(s):
    words = s.split()  # split string into words
    ordered_words = []
    for word in words:
        ordered_word = ''.join(sorted(word))  # sort characters in word
        ordered_words.append(ordered_word)
    return ' '.join(ordered_words)
