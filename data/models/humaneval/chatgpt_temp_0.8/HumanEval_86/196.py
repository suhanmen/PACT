def anti_shuffle(s):
    words = s.split()  # split string into words
    new_words = []
    for word in words:
        sorted_word = ''.join(sorted(word, key=lambda x: ord(x)))  # sort word based on ascii value
        new_words.append(sorted_word)
    return ' '.join(new_words)  # join words with a space and return the ordered string
