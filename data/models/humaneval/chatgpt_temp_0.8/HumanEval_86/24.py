def anti_shuffle(s):
    words = s.split()  # separate words by space
    ordered_words = []
    for word in words:
        ordered_word = ''.join(sorted(word))  # sort characters in ascending order
        ordered_words.append(ordered_word)
    return ' '.join(ordered_words)  # join words by space and return the ordered string
