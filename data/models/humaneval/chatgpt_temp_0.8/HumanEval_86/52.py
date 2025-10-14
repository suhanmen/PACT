def anti_shuffle(s):
    words = s.split()
    new_words = []
    for word in words:
        sorted_word = ''.join(sorted(word))
        new_words.append(sorted_word)
    return ' '.join(new_words)
