def anti_shuffle(s):
    words = s.split()
    ordered_words = []
    for word in words:
        ordered_chars = ''.join(sorted(word))
        ordered_words.append(ordered_chars)
    return ' '.join(ordered_words)
