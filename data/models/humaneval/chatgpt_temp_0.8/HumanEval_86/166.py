def anti_shuffle(s):
    words = s.split()
    ordered_words = []
    for word in words:
        sorted_word = ''.join(sorted(word))
        ordered_words.append(sorted_word)
    return ' '.join(ordered_words)
