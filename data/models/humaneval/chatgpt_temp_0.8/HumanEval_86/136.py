def anti_shuffle(s):
    words = s.split()
    ordered_words = []
    for word in words:
        ordered_word_chars = sorted(word, key=lambda c: ord(c))
        ordered_word = ''.join(ordered_word_chars)
        ordered_words.append(ordered_word)
    return ' '.join(ordered_words)
