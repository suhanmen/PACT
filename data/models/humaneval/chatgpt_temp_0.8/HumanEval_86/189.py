def anti_shuffle(s):
    words = s.split()
    new_words = []
    for word in words:
        sorted_chars = sorted(word, key=lambda c: ord(c))
        new_word = ''.join(sorted_chars)
        new_words.append(new_word)
    return ' '.join(new_words)
