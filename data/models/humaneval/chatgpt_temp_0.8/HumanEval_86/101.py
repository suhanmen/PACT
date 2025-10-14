def anti_shuffle(s):
    words = s.split()
    new_words = []
    for word in words:
        new_word = ''.join(sorted(word))
        new_words.append(new_word)
    return ' '.join(new_words)
